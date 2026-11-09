"""Parse ``manuscript/*/research.md`` files and emit a unified ``references.bib``.

Each ``research.md`` entry follows a uniform Chicago Notes & Bibliography format:

    **Author(s). "Title." *Venue* Volume, no. Issue (Month Year): Pages.**

    - DOI: `10.xxxx/xxxx`     (or URL / ISBN)
    - **Type:** ...
    - **Summary:** ...
    - **Relevance:** ...
    - **How to use:** ...
    - Status: `[ ] Unverified`

Entry chunks are separated by ``---`` horizontal rules in the source files.

CLI
---
``--check``    Dry run; print what would be written, plus a parse-warning report.
``--write``    Write ``references.bib`` (the default for one-shot runs).
``--chapter N`` Restrict to chapter N (for incremental development).
"""

from __future__ import annotations

import argparse
import logging
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter

from tools.citation_keys import generate_key

logger = logging.getLogger("research_to_bibtex")

REPO_ROOT = Path(__file__).resolve().parent.parent
MANUSCRIPT_DIR = REPO_ROOT / "manuscript"
BIB_PATH = MANUSCRIPT_DIR / "99_bibliography" / "references.bib"

# Regexes for the components of a Chicago bold citation line.
RE_BOLD_LINE = re.compile(r"^\*\*(?P<body>.+?)\*\*\s*$", re.DOTALL)
RE_QUOTED_TITLE = re.compile(r'"(?P<title>[^"]+)"')
RE_ITALIC_TITLE = re.compile(r"\*(?P<title>[^*]+)\*")
RE_YEAR = re.compile(r"\b(?P<year>19\d{2}|20\d{2}|21\d{2})\b")
RE_YEAR_IN_PARENS = re.compile(r"\((?:[A-Za-z]+\s+\d+,?\s+|[A-Za-z]+[-–—][A-Za-z]+\s+|[A-Za-z]+\s+)?(?P<year>19\d{2}|20\d{2}|21\d{2})\)")


def _find_year(text: str) -> int | None:
    """Find the publication year in a citation fragment.

    Chicago citations end with the year, so prefer:
      1. Year in parens (e.g., "(2018)") — strongest signal.
      2. Last plausible year (1900-2100) in the string.
    """
    paren_match = RE_YEAR_IN_PARENS.search(text)
    if paren_match:
        return int(paren_match["year"])
    candidates = RE_YEAR.findall(text)
    if candidates:
        return int(candidates[-1])
    return None
RE_PAGES = re.compile(r"(?P<pages>\d+[-–—]\d+|\d+)")
RE_DOI_BULLET = re.compile(r"^\s*-\s*DOI:\s*`?(?P<doi>[^`\s]+)`?", re.IGNORECASE | re.MULTILINE)
RE_URL_BULLET = re.compile(r"^\s*-\s*URL:\s*`?(?P<url>[^`\s]+)`?", re.IGNORECASE | re.MULTILINE)
RE_ISBN_BULLET = re.compile(r"^\s*-\s*ISBN:\s*`?(?P<isbn>[\d\-X]+)`?", re.IGNORECASE | re.MULTILINE)
RE_ARXIV_ID = re.compile(r"arxiv[.:/]+(?:abs/)?(?P<arxiv_id>\d{4}\.\d{4,5}(?:v\d+)?)", re.IGNORECASE)
RE_STATUS_VERIFIED = re.compile(r"^\s*-\s*Status:\s*`?\[x\]\s*Verified", re.IGNORECASE | re.MULTILINE)

# Volume/issue/pages pattern for journal articles:
#   "Journal Name Volume, no. Issue (Month Year): Pages."
# Tolerates: "no." or "nos.", number ranges (1-3), supplement issues,
# month ranges ("July-August"), and page prefixes ("S114-S133").
RE_JOURNAL_DETAILS = re.compile(
    r"\*(?P<journal>[^*]+)\*"
    r"\s*(?P<volume>\d+)"
    r"(?:,\s*(?:nos?\.|Supplement)\s*(?P<number>[A-Za-z]?\d+(?:[-–—]\d+)?))?"
    r"\s*\((?:(?P<month>[A-Z][a-z]+(?:[-–—][A-Z][a-z]+)?(?:\s\d+,?)?)\s+)?(?P<year>\d{4})\)"
    r"\s*:\s*(?P<pages>[A-Za-z]?\d+(?:[-–—][A-Za-z]?\d+)?)"
)

# Conference paper pattern: "In *Booktitle*, Pages. Location: Publisher, Month Year."
RE_CONF_DETAILS = re.compile(
    r"In\s+\*(?P<booktitle>[^*]+)\*"
    r"(?:,\s*(?P<pages>\d+[-–—]\d+))?"
    r"(?:\.\s*(?P<location>[^:.]+):\s*(?P<publisher>[^,.]+))?"
    r"(?:,\s*(?:(?P<month>[A-Z][a-z]+)\s+)?(?P<year>\d{4}))?"
)

# Book pattern: "Location: Publisher, Year."
RE_BOOK_DETAILS = re.compile(
    r"(?P<location>[^:]+):\s*(?P<publisher>[^,]+),\s*(?P<year>\d{4})"
)

# arXiv preprint pattern: "arXiv preprint, arXiv:XXXX.YYYYY, Month Year."
RE_ARXIV_FULL = re.compile(
    r"arXiv\s+preprint,?\s*arXiv:(?P<arxiv_id>\d{4}\.\d{4,5})"
    r"(?:,\s*(?:(?P<month>[A-Z][a-z]+)\s+)?(?P<year>\d{4}))?",
    re.IGNORECASE,
)


@dataclass
class ParseWarning:
    chapter: str
    line_no: int
    message: str
    raw: str = ""


@dataclass
class RawEntry:
    """A parsed entry before BibTeX serialization."""

    chapter: str
    line_no: int
    raw_bold_line: str
    authors: list[str] = field(default_factory=list)
    title: str = ""
    year: int | None = None
    entry_type: str = "article"
    fields: dict[str, str] = field(default_factory=dict)
    identifiers: dict[str, str] = field(default_factory=dict)
    verified: bool = False
    warnings: list[str] = field(default_factory=list)

    @property
    def fingerprint(self) -> tuple[str, int | None, str]:
        """Hash for deduplication across chapters."""
        first_surname = ""
        if self.authors:
            first = self.authors[0]
            first_surname = first.split(",", 1)[0].strip().lower() if "," in first else first.lower()
        title_head = re.sub(r"[^a-z0-9 ]", "", self.title.lower())[:50]
        return (first_surname, self.year, title_head)


# ---------- Author parsing ----------


def _flip_to_bibtex(first_last: str) -> str:
    """Convert ``First Middle Last`` to ``Last, First Middle``."""
    parts = first_last.strip().split()
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    return f"{parts[-1]}, {' '.join(parts[:-1])}"


def _is_organizational(token: str) -> bool:
    org_signals = {
        "commission", "bank", "department", "ministry", "office", "bureau",
        "federation", "association", "society", "institute", "fund", "reserve",
        "treasury", "exchange", "authority", "board", "council", "agency",
    }
    return bool({w.lower() for w in re.findall(r"[A-Za-z]+", token)} & org_signals)


def parse_authors(author_block: str) -> list[str]:
    """Parse a Chicago author string into BibTeX ``Last, First`` form.

    Handles:
    - Single author: ``Fama, Eugene F.`` → ``["Fama, Eugene F."]``
    - Two authors: ``Loughran, Tim, and Bill McDonald`` → both
    - Three+ authors (Oxford comma): ``Gentzkow, Matthew, Bryan Kelly, and Matt Taddy``
    - "et al." compressions
    - Organizational authors (no comma, has institution words)
    """
    block = author_block.rstrip(".").strip()

    # Organizational author (no comma; just the institution name)
    if "," not in block and _is_organizational(block):
        return [block]

    # Handle "et al."
    if re.search(r"\bet al\.?\s*$", block, re.IGNORECASE):
        prefix = re.sub(r"\s*,?\s*et al\.?\s*$", "", block, flags=re.IGNORECASE).strip()
        first = prefix.split(",", 2)
        if len(first) >= 2:
            return [f"{first[0]}, {first[1]}", "others"]
        return [prefix, "others"]

    # Split on ", and " (Oxford comma form) or " and " (two-author form)
    if ", and " in block:
        before, last_first_last = block.rsplit(", and ", 1)
        middle_parts = before.split(", ")
    elif " and " in block:
        before, last_first_last = block.rsplit(" and ", 1)
        middle_parts = before.split(", ")
    else:
        # Single author in "Last, First" form
        return [block]

    # Reconstruct first author from first two comma-separated parts
    if len(middle_parts) >= 2:
        first_author = f"{middle_parts[0]}, {middle_parts[1]}"
        middle_first_last = middle_parts[2:]
    else:
        first_author = middle_parts[0]
        middle_first_last = []

    authors = [first_author]
    authors.extend(_flip_to_bibtex(a) for a in middle_first_last)
    authors.append(_flip_to_bibtex(last_first_last))
    return [a for a in authors if a]


# ---------- Citation line parsing ----------


def _normalize_pages(pages: str) -> str:
    """Convert en/em dashes to ``--`` for BibTeX."""
    return re.sub(r"[–—-]+", "--", pages.strip()) if pages else ""


_MONTH_MAP: dict[str, str] = {
    "january": "1", "jan": "1",
    "february": "2", "feb": "2",
    "march": "3", "mar": "3",
    "april": "4", "apr": "4",
    "may": "5",
    "june": "6", "jun": "6",
    "july": "7", "jul": "7",
    "august": "8", "aug": "8",
    "september": "9", "sep": "9", "sept": "9",
    "october": "10", "oct": "10",
    "november": "11", "nov": "11",
    "december": "12", "dec": "12",
}


def _normalize_month(month_text: str | None) -> str | None:
    """Convert a Chicago-style month/season fragment into a biber-preferred numeric.

    Returns the numeric month string (e.g., ``"6"``) for English month names.
    Returns ``None`` for seasons (Spring/Summer/Fall/Winter) — biblatex prefers
    the ``season`` field for those, and we skip rather than emit invalid data.
    """
    if not month_text:
        return None
    # Take the first word (handles "January 15" or "July-August" first half).
    first_word = re.split(r"[\s\-–—]", month_text.strip(), maxsplit=1)[0].lower()
    return _MONTH_MAP.get(first_word)


def parse_citation_line(bold_body: str) -> dict[str, str | list[str]]:
    """Parse the body of a bold citation line into structured fields.

    Returns a dict with ``authors``, ``title``, ``year``, ``entry_type``,
    ``fields`` (BibTeX-shaped dict), plus any parse-time warnings under
    a ``_warnings`` key.
    """
    body = bold_body.strip()
    warnings: list[str] = []
    out: dict[str, str | list[str]] = {"_warnings": warnings}

    # arXiv preprint? (most specific — matches before article)
    arxiv_match = RE_ARXIV_FULL.search(body)
    if arxiv_match:
        out["entry_type"] = "misc"
        title_match = RE_QUOTED_TITLE.search(body)
        if not title_match:
            warnings.append("arxiv entry missing quoted title")
            return out
        title = title_match["title"].rstrip(". ")
        # Authors are everything before the first opening quote
        author_block = body[: title_match.start()].rstrip(' "').rstrip(".")
        year = arxiv_match["year"] or _find_year(body) or 0
        out["authors"] = parse_authors(author_block)
        out["title"] = title
        out["year"] = int(year)
        out["fields"] = {
            "howpublished": f"arXiv preprint, arXiv:{arxiv_match['arxiv_id']}",
            "eprint": arxiv_match["arxiv_id"],
            "eprinttype": "arxiv",
            "url": f"https://arxiv.org/abs/{arxiv_match['arxiv_id']}",
        }
        month_num = _normalize_month(arxiv_match["month"])
        if month_num:
            out["fields"]["month"] = month_num
        return out

    # Article, conference, or web report? (quoted title present)
    quoted = RE_QUOTED_TITLE.search(body)
    if quoted:
        title = quoted["title"].rstrip(". ")
        author_block = body[: quoted.start()].rstrip(' "').rstrip(".")
        details_body = body[quoted.end() :].lstrip('".').strip()

        # Conference paper signal: "In *Booktitle*..." or "In *Proceedings of...*"
        if re.match(r"\.?\s*In\s+\*", details_body):
            return _parse_conference(author_block, title, details_body, warnings)

        # No italicized venue at all → web doc / report (not @article)
        if not RE_ITALIC_TITLE.search(details_body):
            return _parse_web_doc(author_block, title, details_body, warnings)

        # Has italicized venue → journal article (or working paper)
        return _parse_article(author_block, title, details_body, warnings)

    # Book or legal case? (italicized standalone title, no quoted title)
    italic = RE_ITALIC_TITLE.search(body)
    if italic:
        title = italic["title"].rstrip(". ")
        author_block = body[: italic.start()].rstrip(' "').rstrip(".")
        details_body = body[italic.end() :].strip(".").strip()
        # Legal cases match "X v. Y" or "X v Y" in the italicized title
        if re.search(r"\bv\.\s*", title, re.IGNORECASE):
            return _parse_legal_case(title, details_body, warnings)
        return _parse_book(author_block, title, details_body, warnings)

    warnings.append("could not identify entry type (no quoted or italic title)")
    return out


def _parse_web_doc(
    author_block: str, title: str, details: str, warnings: list[str]
) -> dict[str, str | list[str]]:
    """Parse web documents, reports, and regulatory pages (no italicized venue)."""
    out: dict[str, str | list[str]] = {
        "entry_type": "misc",  # _refine_entry_type may bump to @online
        "title": title,
        "_warnings": warnings,
    }
    out["authors"] = parse_authors(author_block)
    year = _find_year(details)
    if year is not None:
        out["year"] = year
    out["fields"] = {"howpublished": details.strip().rstrip(".")}
    return out


def _parse_legal_case(
    title: str, details: str, warnings: list[str]
) -> dict[str, str | list[str]]:
    """Parse U.S. case citations: ``*X v. Y*, Reporter Citation (Year).``"""
    out: dict[str, str | list[str]] = {
        "entry_type": "misc",
        "title": title,
        "authors": [],
        "_warnings": warnings,
    }
    year = _find_year(details)
    if year is not None:
        out["year"] = year
    # Author for legal case is conventionally the case name; biblatex prefers the title carry it.
    out["authors"] = ["{Legal Case}"]
    out["fields"] = {"howpublished": details.strip().rstrip(".") or "Court reporter citation"}
    return out


def _parse_article(
    author_block: str, title: str, details: str, warnings: list[str]
) -> dict[str, str | list[str]]:
    out: dict[str, str | list[str]] = {
        "entry_type": "article",
        "title": title,
        "_warnings": warnings,
    }
    # Always parse authors first — type-specific parsing only enriches
    out["authors"] = parse_authors(author_block)

    # Detect non-journal venues that came through with quoted titles
    details_lower = details.lower()
    if "working paper" in details_lower or "research working paper" in details_lower:
        return _parse_working_paper(details, out)
    if "thesis" in details_lower or "dissertation" in details_lower:
        return _parse_thesis(details, out)

    journal_match = RE_JOURNAL_DETAILS.search(details)
    if not journal_match:
        # Try a looser pattern: just an italicized journal + year
        journal_loose = RE_ITALIC_TITLE.search(details)
        if journal_loose:
            out["fields"] = {"journaltitle": journal_loose["title"].strip().rstrip(".")}
            year = _find_year(details)
            if year is not None:
                out["year"] = year
            warnings.append("article missing volume/issue/pages — used loose journal+year match")
        else:
            warnings.append("article: could not parse journal details — falling back to @misc")
            out["entry_type"] = "misc"
            year = _find_year(details)
            if year is not None:
                out["year"] = year
            out["fields"] = {"howpublished": details.strip().rstrip(".") or "Unknown venue"}
        return out

    fields = {
        "journaltitle": journal_match["journal"].strip().rstrip(","),
        "volume": journal_match["volume"],
    }
    if journal_match["number"]:
        fields["number"] = journal_match["number"]
    if journal_match["pages"]:
        fields["pages"] = _normalize_pages(journal_match["pages"])
    month_num = _normalize_month(journal_match["month"])
    if month_num:
        fields["month"] = month_num
    out["fields"] = fields
    out["year"] = int(journal_match["year"])
    return out


def _parse_working_paper(details: str, out: dict) -> dict:
    """Parse a working-paper venue: Federal Reserve Bank of X Research Working Paper no. Y."""
    out["entry_type"] = "techreport"
    fields: dict[str, str] = {}
    # Try to extract the institution and paper number
    inst_match = re.search(
        r"(?P<institution>(?:Federal Reserve|National Bureau|Bank of [\w\s]+|[\w\s]+University|[\w\s]+Institute)[\w\s,]+?)"
        r"\s+(?:Research\s+)?Working Paper(?:\s+no\.\s*(?P<number>[\w\-]+))?",
        details,
        re.IGNORECASE,
    )
    if inst_match:
        fields["institution"] = inst_match["institution"].strip()
        if inst_match["number"]:
            fields["number"] = inst_match["number"]
    else:
        fields["howpublished"] = details.strip().rstrip(".")
    year = _find_year(details)
    if year is not None:
        out["year"] = year
    out["fields"] = fields
    return out


def _parse_thesis(details: str, out: dict) -> dict:
    """Parse thesis/dissertation entries."""
    details_lower = details.lower()
    out["entry_type"] = "phdthesis" if "phd" in details_lower or "dissertation" in details_lower else "mastersthesis"
    # If it's an "Honors thesis" treat as misc — biblatex has no honorsthesis
    if "honors thesis" in details_lower:
        out["entry_type"] = "misc"
        out["fields"] = {"howpublished": details.strip().rstrip(".")}
    else:
        fields: dict[str, str] = {}
        school_match = re.search(r"thesis,\s*(?P<school>[^,.]+)", details, re.IGNORECASE)
        if school_match:
            fields["school"] = school_match["school"].strip()
        out["fields"] = fields
    year = _find_year(details)
    if year is not None:
        out["year"] = year
    return out


def _parse_conference(
    author_block: str, title: str, details: str, warnings: list[str]
) -> dict[str, str | list[str]]:
    out: dict[str, str | list[str]] = {
        "entry_type": "inproceedings",
        "title": title,
        "_warnings": warnings,
    }
    # Parse authors first — type-specific parsing only enriches
    out["authors"] = parse_authors(author_block)
    conf_match = RE_CONF_DETAILS.search(details)
    if not conf_match:
        warnings.append("conference: could not parse booktitle/pages")
        # Still try to capture year so the entry isn't dropped
        year = _find_year(details)
        if year is not None:
            out["year"] = year
        booktitle_match = RE_ITALIC_TITLE.search(details)
        if booktitle_match:
            out["fields"] = {"booktitle": booktitle_match["title"].strip().rstrip(",")}
        return out
    fields: dict[str, str] = {"booktitle": conf_match["booktitle"].strip().rstrip(",")}
    if conf_match["pages"]:
        fields["pages"] = _normalize_pages(conf_match["pages"])
    if conf_match["location"]:
        fields["location"] = conf_match["location"].strip()
    if conf_match["publisher"]:
        fields["publisher"] = conf_match["publisher"].strip()
    month_num = _normalize_month(conf_match["month"])
    if month_num:
        fields["month"] = month_num
    out["fields"] = fields
    out["year"] = int(conf_match["year"]) if conf_match["year"] else None
    if out["year"] is None:
        year = _find_year(details)
        if year is not None:
            out["year"] = year
    return out


def _parse_book(
    author_block: str, title: str, details: str, warnings: list[str]
) -> dict[str, str | list[str]]:
    out: dict[str, str | list[str]] = {
        "entry_type": "book",
        "title": title,
        "_warnings": warnings,
    }
    # Parse authors first
    out["authors"] = parse_authors(author_block)
    book_match = RE_BOOK_DETAILS.search(details)
    if book_match:
        out["fields"] = {
            "location": book_match["location"].strip(),
            "publisher": book_match["publisher"].strip(),
        }
        out["year"] = int(book_match["year"])
    else:
        year = _find_year(details)
        if year is not None:
            out["year"] = year
        # Try to pull publisher as "Publisher, Year"
        pub_match = re.search(r"(?P<publisher>[^,]+),\s*\d{4}", details)
        if pub_match:
            out["fields"] = {"publisher": pub_match["publisher"].strip()}
        else:
            warnings.append("book: could not parse location/publisher")
            out["fields"] = {}
    return out


# ---------- Identifier extraction & entry-type override ----------


def extract_identifiers(chunk: str) -> dict[str, str]:
    """Pull DOI / URL / ISBN bullets from an entry chunk."""
    ids: dict[str, str] = {}
    for pattern, key in [(RE_DOI_BULLET, "doi"), (RE_URL_BULLET, "url"), (RE_ISBN_BULLET, "isbn")]:
        m = pattern.search(chunk)
        if m:
            ids[key] = m[key].strip(".,;")
    return ids


def _refine_entry_type(parsed: dict, identifiers: dict[str, str]) -> str:
    """Apply identifier signals to refine the type chosen from the citation line."""
    current = parsed.get("entry_type", "article")
    url = identifiers.get("url", "").lower()

    # arXiv URL on something we didn't already classify as misc → reclassify as misc
    if "arxiv" in url and current == "article":
        return "misc"

    # ISBN present → book (overrides article/inproceedings if mis-detected)
    if "isbn" in identifiers and current not in {"book", "incollection"}:
        return "book"

    # No DOI, URL on a regulatory / institutional domain → @online
    if current in {"article", "misc"} and "doi" not in identifiers and url and "arxiv" not in url:
        institutional_domains = (
            "sec.gov", "federalreserve.gov", "ecb.europa.eu",
            "fraser.stlouisfed.org", "stlouisfed.org", ".gov", ".eu",
            "github.com", "wikipedia.org", "econlib.org", "aeaweb.org",
            "imf.org", "bis.org", "huggingface.co", "finra.org",
            "nist.gov", "europarl.europa.eu",
        )
        if any(d in url for d in institutional_domains):
            return "online"
    return current


# ---------- Top-level pipeline ----------


def _split_entry_chunks(text: str) -> list[tuple[int, str]]:
    """Split a research.md file into ``(approx_line_no, chunk_text)`` tuples.

    Each chunk is the text between ``---`` horizontal rules. Section headers
    (lines starting with ``#``) appearing on their own without a bold citation
    line are filtered out by the caller.
    """
    lines = text.splitlines(keepends=True)
    chunks: list[tuple[int, str]] = []
    buffer: list[str] = []
    chunk_start_line = 1
    for i, line in enumerate(lines, start=1):
        if line.strip() == "---":
            if buffer:
                chunks.append((chunk_start_line, "".join(buffer)))
                buffer = []
            chunk_start_line = i + 1
        else:
            buffer.append(line)
    if buffer:
        chunks.append((chunk_start_line, "".join(buffer)))
    return chunks


def _find_bold_line(chunk: str) -> str | None:
    """Find the first bold-wrapped paragraph in a chunk (the citation line).

    Bold citation lines are multi-line in some entries. We treat any
    paragraph that begins with ``**`` and ends with ``**`` as the citation.
    """
    # Look for ``**...**`` spanning a paragraph (no blank line inside).
    paragraphs = re.split(r"\n\s*\n", chunk)
    for para in paragraphs:
        para = para.strip()
        if para.startswith("**") and "**" in para[2:]:
            # Strip a possible leading list marker and grab the bold span
            m = re.search(r"\*\*(.+?)\*\*", para, re.DOTALL)
            if m:
                body = m.group(1).strip()
                # Filter out very short bolds — they're labels (e.g., "**Summary:**")
                if len(body) > 40 and ('"' in body or re.search(r"\*[^*]+\*", body)):
                    return body
    return None


def parse_chapter(path: Path) -> tuple[list[RawEntry], list[ParseWarning]]:
    """Parse one research.md file into RawEntry list + warnings."""
    chapter_slug = path.parent.name[:5].lower().replace("_", "")  # e.g., "01_wh..." -> "01wh"
    # Use first two chars as the canonical "chNN" tag
    ch_num = path.parent.name[:2]
    chapter_tag = f"ch{ch_num}"

    text = path.read_text(encoding="utf-8")
    chunks = _split_entry_chunks(text)
    entries: list[RawEntry] = []
    warnings: list[ParseWarning] = []

    for line_no, chunk in chunks:
        bold_body = _find_bold_line(chunk)
        if not bold_body:
            continue

        parsed = parse_citation_line(bold_body)
        identifiers = extract_identifiers(chunk)
        verified = bool(RE_STATUS_VERIFIED.search(chunk))

        # Refine entry type using identifier signals
        if "entry_type" in parsed:
            parsed["entry_type"] = _refine_entry_type(parsed, identifiers)

        raw = RawEntry(
            chapter=chapter_tag,
            line_no=line_no,
            raw_bold_line=bold_body,
            authors=parsed.get("authors", []),
            title=parsed.get("title", ""),
            year=parsed.get("year"),
            entry_type=parsed.get("entry_type", "article"),
            fields=parsed.get("fields", {}),
            identifiers=identifiers,
            verified=verified,
        )

        # Surface warnings
        for w in parsed.get("_warnings", []):
            warnings.append(ParseWarning(chapter_tag, line_no, w, bold_body[:120]))
        if not raw.authors:
            warnings.append(ParseWarning(chapter_tag, line_no, "no authors parsed", bold_body[:120]))
            continue
        if not raw.year:
            warnings.append(ParseWarning(chapter_tag, line_no, "no year parsed", bold_body[:120]))
            continue
        if not raw.title:
            warnings.append(ParseWarning(chapter_tag, line_no, "no title parsed", bold_body[:120]))
            continue

        entries.append(raw)

    return entries, warnings


def merge_duplicates(entries: list[RawEntry]) -> list[RawEntry]:
    """Merge entries that fingerprint the same paper across chapters.

    Anchor sources (Loughran-McDonald, Tetlock, etc.) appear in many
    research.md files; we keep one canonical entry whose ``chapter`` field
    becomes a sorted list of all chapters citing it. The entry with the
    richest metadata (DOI > URL > ISBN, more fields wins ties) is preferred.
    """
    by_fp: dict[tuple, list[RawEntry]] = defaultdict(list)
    for e in entries:
        by_fp[e.fingerprint].append(e)

    merged: list[RawEntry] = []
    for fp, group in by_fp.items():
        if len(group) == 1:
            merged.append(group[0])
            continue
        # Pick canonical entry: prefer DOI > URL > ISBN, then richest fields
        def richness(e: RawEntry) -> tuple:
            id_score = 3 if "doi" in e.identifiers else 2 if "url" in e.identifiers else 1
            return (id_score, len(e.fields), e.verified)
        canonical = max(group, key=richness)
        canonical.chapter = ",".join(sorted({e.chapter for e in group}))
        canonical.verified = any(e.verified for e in group)
        merged.append(canonical)

    return merged


def _assign_keys(entries: list[RawEntry]) -> dict[str, RawEntry]:
    """Assign citation keys to entries, resolving collisions with title keyword.

    Returns a dict ``key → entry``.
    """
    by_key: dict[str, RawEntry] = {}
    pending_collisions: list[RawEntry] = []

    for e in entries:
        key = generate_key(e.authors, e.year, e.title)
        if key in by_key:
            pending_collisions.append(e)
            # Also mark the existing entry for disambiguation
            existing = by_key.pop(key)
            pending_collisions.append(existing)
        else:
            by_key[key] = e

    for e in pending_collisions:
        new_key = generate_key(e.authors, e.year, e.title, disambiguator="title")
        # If still colliding, append "_alt"
        attempt = 1
        candidate = new_key
        while candidate in by_key:
            candidate = f"{new_key}_alt{attempt}"
            attempt += 1
        by_key[candidate] = e

    # Special override: two FinBERTs need explicit suffix per CITATIONS.md §"Two FinBERTs"
    def _needs_finbert_suffix(entry: RawEntry) -> bool:
        if not entry.authors or "finbert" not in entry.title.lower():
            return False
        first_surname = entry.authors[0].split(",", 1)[0].strip()
        return first_surname in ("Araci", "Huang")

    finbert_renames: list[tuple[str, str]] = []
    for k, e in by_key.items():
        if _needs_finbert_suffix(e) and "_finbert" not in k:
            new_key = f"{k}_finbert"
            finbert_renames.append((k, new_key))

    for old_key, new_key in finbert_renames:
        # Resolve final collisions on the renamed key
        final_key = new_key
        attempt = 1
        while final_key in by_key and final_key != old_key:
            final_key = f"{new_key}_alt{attempt}"
            attempt += 1
        by_key[final_key] = by_key.pop(old_key)

    return by_key


def _to_bibtex_dict(key: str, entry: RawEntry) -> dict[str, str]:
    """Convert a RawEntry into the dict shape bibtexparser expects."""
    bib: dict[str, str] = {
        "ENTRYTYPE": entry.entry_type,
        "ID": key,
    }
    # Authors
    if entry.authors:
        # Wrap purely organizational author with double braces to prevent name parsing
        if len(entry.authors) == 1 and "," not in entry.authors[0]:
            bib["author"] = f"{{{{{entry.authors[0]}}}}}"
        else:
            bib["author"] = " and ".join(entry.authors)
    # Core fields
    bib["title"] = entry.title
    bib["year"] = str(entry.year)
    bib.update(entry.fields)
    # Identifiers
    if "doi" in entry.identifiers:
        bib["doi"] = entry.identifiers["doi"]
    if "url" in entry.identifiers and "url" not in bib:
        bib["url"] = entry.identifiers["url"]
    if "isbn" in entry.identifiers:
        bib["isbn"] = entry.identifiers["isbn"]
    # Chapter affiliations
    bib["keywords"] = entry.chapter
    return bib


def write_bibfile(entries: dict[str, RawEntry], path: Path) -> int:
    """Emit a sorted, grouped-by-entry-type references.bib file. Returns entry count."""
    db = BibDatabase()
    # Group by entry type, then sort by key within each group
    by_type: dict[str, list[tuple[str, RawEntry]]] = defaultdict(list)
    for key, entry in entries.items():
        by_type[entry.entry_type].append((key, entry))

    type_order = ["article", "book", "inproceedings", "incollection", "misc", "online"]
    sorted_keys: list[tuple[str, RawEntry]] = []
    for t in type_order:
        sorted_keys.extend(sorted(by_type.get(t, []), key=lambda kv: kv[0]))
    # Any unrecognized types last
    for t in sorted(set(by_type.keys()) - set(type_order)):
        sorted_keys.extend(sorted(by_type[t], key=lambda kv: kv[0]))

    db.entries = [_to_bibtex_dict(k, e) for k, e in sorted_keys]

    writer = BibTexWriter()
    writer.indent = "    "
    writer.align_values = True
    writer.order_entries_by = None  # we already ordered them

    header = (
        "% Applied NLP for Finance — Bibliography\n"
        "% Citation style: Chicago 17 (Notes and Bibliography), via biblatex-chicago\n"
        "% Keys: lastname_year[_keyword]. See CITATIONS.md.\n"
        "% Generated from manuscript/*/research.md via tools/research_to_bibtex.py\n"
        "% DO NOT hand-edit individual entries — edit research.md and regenerate.\n\n"
    )
    body = writer.write(db)
    path.write_text(header + body, encoding="utf-8")
    return len(db.entries)


# ---------- CLI ----------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--check", action="store_true", help="Dry run; do not write.")
    parser.add_argument("--write", action="store_true", help="Write references.bib.")
    parser.add_argument("--chapter", type=int, help="Restrict to chapter N.")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    # Discover research.md files
    pattern = (
        f"{args.chapter:02d}_*/research.md" if args.chapter is not None else "[0-9][0-9]_*/research.md"
    )
    files = sorted(MANUSCRIPT_DIR.glob(pattern))
    if not files:
        logger.error("No research.md files found under %s with pattern %s", MANUSCRIPT_DIR, pattern)
        return 2

    # Parse all chapters
    all_entries: list[RawEntry] = []
    all_warnings: list[ParseWarning] = []
    for f in files:
        entries, warnings = parse_chapter(f)
        all_entries.extend(entries)
        all_warnings.extend(warnings)
        logger.info("Parsed %3d entries, %2d warnings from %s", len(entries), len(warnings), f.relative_to(REPO_ROOT))

    # Dedup
    pre_dedup = len(all_entries)
    merged = merge_duplicates(all_entries)
    logger.info("Merged %d duplicates → %d unique entries", pre_dedup - len(merged), len(merged))

    # Assign keys
    keyed = _assign_keys(merged)

    # Report warnings
    if all_warnings:
        print("\n=== Parse warnings ===", file=sys.stderr)
        for w in all_warnings:
            print(f"  [{w.chapter}:{w.line_no}] {w.message}\n    {w.raw}", file=sys.stderr)
        print(f"Total warnings: {len(all_warnings)}\n", file=sys.stderr)

    if args.check:
        print(f"\nWould write {len(keyed)} entries to {BIB_PATH.relative_to(REPO_ROOT)}")
        # Group counts by entry type
        type_counts: dict[str, int] = defaultdict(int)
        for e in keyed.values():
            type_counts[e.entry_type] += 1
        for t, c in sorted(type_counts.items()):
            print(f"  @{t}: {c}")
        return 0 if not all_warnings else 1

    if args.write or (not args.check and not args.chapter):
        count = write_bibfile(keyed, BIB_PATH)
        print(f"Wrote {count} entries to {BIB_PATH.relative_to(REPO_ROOT)}")
        return 0

    print("No action specified. Use --check or --write.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
