"""Tests for ``tools.citation_keys``."""

from __future__ import annotations

import pytest

from tools.citation_keys import (
    ascii_fold,
    generate_key,
    surname,
    title_keyword,
)


class TestAsciiFold:
    """The ``ascii_fold`` helper folds accents, strips punctuation, lowercases."""

    @pytest.mark.parametrize(
        ("raw", "expected"),
        [
            ("García", "garcia"),
            ("O'Reilly", "oreilly"),
            ("Saar-Tsechansky", "saartsechansky"),
            ("François", "francois"),
            ("Müller", "muller"),
            ("loughran_mcdonald", "loughran_mcdonald"),  # underscore preserved
            ("MIXED Case", "mixedcase"),
            ("  spaces  ", "spaces"),
            ("d'Aspremont", "daspremont"),
            ("Ñoño", "nono"),
            ("", ""),
        ],
    )
    def test_folds_correctly(self, raw: str, expected: str) -> None:
        assert ascii_fold(raw) == expected


class TestSurname:
    """``surname`` extracts and folds the last name."""

    @pytest.mark.parametrize(
        ("author", "expected"),
        [
            ("Fama, Eugene F.", "fama"),
            ("García, Diego", "garcia"),
            ("McDonald, Bill", "mcdonald"),
            ("O'Reilly, Tim", "oreilly"),
            ("Saar-Tsechansky, Maytal", "saartsechansky"),
            ("Van Der Berg, Maria", "vanderberg"),
            ("Eugene F. Fama", "fama"),  # First Last fallback form
            ("", ""),
        ],
    )
    def test_extracts_surname(self, author: str, expected: str) -> None:
        assert surname(author) == expected


class TestTitleKeyword:
    """``title_keyword`` picks the first non-stopword from the main title."""

    @pytest.mark.parametrize(
        ("title", "expected"),
        [
            ("Prospect Theory: An Analysis of Decision under Risk", "prospect"),
            ("The Framing of Decisions and the Psychology of Choice", "framing"),
            ("On the Impossibility of Informationally Efficient Markets", "impossibility"),
            ("A Survey of Deep Learning for Finance", "survey"),
            ("Narrative Economics", "narrative"),
            ("The Use of Knowledge in Society", "use"),
        ],
    )
    def test_picks_first_content_word(self, title: str, expected: str) -> None:
        assert title_keyword(title) == expected

    def test_strips_subtitle(self) -> None:
        full = "Prospect Theory: An Analysis of Decision under Risk"
        # The disambiguator should come from the main title, not the subtitle.
        assert title_keyword(full) == "prospect"

    def test_empty_title(self) -> None:
        assert title_keyword("") == ""

    def test_only_stopwords(self) -> None:
        # All words are stopwords — falls back to the first word folded.
        assert title_keyword("The and of") == "the"


class TestGenerateKey:
    """``generate_key`` produces the canonical citation key per CITATIONS.md."""

    def test_single_author(self) -> None:
        assert generate_key(["Fama, Eugene F."], 1970) == "fama_1970"
        assert generate_key(["Tetlock, Paul C."], 2007) == "tetlock_2007"
        assert generate_key(["Shiller, Robert J."], 2017) == "shiller_2017"

    def test_two_authors(self) -> None:
        assert (
            generate_key(["Loughran, Tim", "McDonald, Bill"], 2011)
            == "loughran_mcdonald_2011"
        )
        assert (
            generate_key(["Grossman, Sanford J.", "Stiglitz, Joseph E."], 1980)
            == "grossman_stiglitz_1980"
        )

    def test_three_authors_uses_etal(self) -> None:
        assert (
            generate_key(["Gentzkow, Matthew", "Kelly, Bryan", "Taddy, Matt"], 2019)
            == "gentzkow_etal_2019"
        )

    def test_many_authors_uses_etal(self) -> None:
        authors = [f"Author{i}, First" for i in range(7)]
        assert generate_key(authors, 2024) == "author0_etal_2024"

    def test_accented_surname(self) -> None:
        assert generate_key(["García, Diego"], 2013) == "garcia_2013"

    def test_apostrophe_in_surname(self) -> None:
        assert generate_key(["O'Reilly, Tim"], 2020) == "oreilly_2020"

    def test_hyphenated_surname(self) -> None:
        assert (
            generate_key(["Tetlock, Paul C.", "Saar-Tsechansky, Maytal"], 2008)
            == "tetlock_saartsechansky_2008"
        )

    def test_organizational_author(self) -> None:
        assert (
            generate_key(["Securities and Exchange Commission"], 2025) == "sec_2025"
        )
        assert (
            generate_key(["Federal Reserve Bank of St Louis"], 2026)
            == "frbsl_2026"
        )

    def test_organizational_parenthetical_abbreviation(self) -> None:
        """Parenthetical abbreviations win over initials.

        ``Financial Industry Regulatory Authority (FINRA)`` should use FINRA.
        """
        assert (
            generate_key(
                ["Financial Industry Regulatory Authority (FINRA)"], 2026
            )
            == "finra_2026"
        )
        assert (
            generate_key(
                ["Alternative Investment Management Association (AIMA)"], 2024
            )
            == "aima_2024"
        )

    def test_et_al_authors_use_etal_key(self) -> None:
        """When authors include 'others' (BibTeX et al. marker), use _etal_ pattern."""
        assert (
            generate_key(["Pfeffer, Jürgen", "others"], 2024) == "pfeffer_etal_2024"
        )

    def test_disambiguator_title(self) -> None:
        assert (
            generate_key(
                ["Kahneman, Daniel", "Tversky, Amos"],
                1979,
                title="Prospect Theory: An Analysis of Decision under Risk",
                disambiguator="title",
            )
            == "kahneman_tversky_1979_prospect"
        )
        assert (
            generate_key(
                ["Kahneman, Daniel", "Tversky, Amos"],
                1981,
                title="The Framing of Decisions and the Psychology of Choice",
                disambiguator="title",
            )
            == "kahneman_tversky_1981_framing"
        )

    def test_disambiguator_literal_string(self) -> None:
        assert (
            generate_key(
                ["Araci, Dogu"],
                2019,
                disambiguator="finbert",
            )
            == "araci_2019_finbert"
        )

    def test_collision_pair_in_research_review(self) -> None:
        """The two FinBERTs scenario from research_review.md §7.3 — they must get distinct keys."""
        araci = generate_key(["Araci, Dogu"], 2019, disambiguator="finbert")
        huang = generate_key(
            ["Huang, Allen H.", "Wang, Hui", "Yang, Yi"],
            2023,
            disambiguator="finbert",
        )
        assert araci == "araci_2019_finbert"
        assert huang == "huang_etal_2023_finbert"
        assert araci != huang

    def test_empty_authors_raises(self) -> None:
        with pytest.raises(ValueError, match="At least one author"):
            generate_key([], 2020)

    def test_anchor_sources_from_research_review(self) -> None:
        """The 11 cross-cutting anchor sources should all generate unique, stable keys."""
        anchors = {
            ("Loughran, Tim", "McDonald, Bill", 2011): "loughran_mcdonald_2011",
            ("Tetlock, Paul C.", None, 2007): "tetlock_2007",
            ("Shiller, Robert J.", None, 2017): "shiller_2017",
            ("García, Diego", None, 2013): "garcia_2013",
            ("Baker, Malcolm", "Wurgler, Jeffrey", 2006): "baker_wurgler_2006",
            ("Manela, Asaf", "Moreira, Alan", 2017): "manela_moreira_2017",
            ("McLean, R. David", "Pontiff, Jeffrey", 2016): "mclean_pontiff_2016",
        }
        for (a1, a2, year), expected in anchors.items():
            authors = [a1] + ([a2] if a2 else [])
            assert generate_key(authors, year) == expected
