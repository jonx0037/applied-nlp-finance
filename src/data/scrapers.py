"""Scrapers and API wrappers for financial text data sources."""

from __future__ import annotations

from pathlib import Path


class SECEdgarScraper:
    """Wrapper for SEC EDGAR full-text search and filing downloads.

    Uses the SEC EDGAR EFTS (full-text search) API and filing archives
    to retrieve 10-K, 10-Q, 8-K, and other SEC filings programmatically.

    Parameters
    ----------
    user_agent : str
        A user-agent string identifying the requester (required by SEC).
        Format: ``"Company Name admin@example.com"``.
    """

    def __init__(self, user_agent: str) -> None:
        # TODO: implement — store user_agent and configure an HTTP session
        # with appropriate rate-limiting headers required by SEC EDGAR.
        self.user_agent = user_agent

    def download_filing(
        self,
        ticker: str,
        filing_type: str,
        *,
        date_after: str | None = None,
        date_before: str | None = None,
        output_dir: Path | None = None,
    ) -> Path:
        """Download a specific SEC filing to disk.

        Parameters
        ----------
        ticker : str
            Company ticker symbol (e.g. ``"AAPL"``).
        filing_type : str
            SEC filing type (e.g. ``"10-K"``, ``"10-Q"``, ``"8-K"``).
        date_after : str | None
            Only consider filings after this date (``YYYY-MM-DD``).
        date_before : str | None
            Only consider filings before this date (``YYYY-MM-DD``).
        output_dir : Path | None
            Directory to save the downloaded file. Defaults to current dir.

        Returns
        -------
        Path
            Path to the downloaded filing file.
        """
        # TODO: implement — resolve CIK from ticker, query EDGAR for the
        # filing index, download the primary document, and save to disk.
        raise NotImplementedError

    def search_filings(
        self,
        query: str,
        *,
        filing_type: str | None = None,
        date_range: tuple[str, str] | None = None,
        max_results: int = 50,
    ) -> list[dict]:
        """Search SEC EDGAR full-text search for filings matching a query.

        Parameters
        ----------
        query : str
            Full-text search query.
        filing_type : str | None
            Optional filter by filing type.
        date_range : tuple[str, str] | None
            Optional ``(start_date, end_date)`` filter.
        max_results : int
            Maximum number of results to return.

        Returns
        -------
        list[dict]
            List of filing metadata dictionaries with keys such as
            ``"accession_number"``, ``"filing_date"``, ``"company_name"``,
            ``"filing_type"``, ``"url"``.
        """
        # TODO: implement — call SEC EDGAR EFTS API, parse results,
        # handle pagination, and return structured metadata.
        raise NotImplementedError

    def get_filing_text(self, url: str) -> str:
        """Retrieve the plain-text content of a filing given its URL.

        Parameters
        ----------
        url : str
            URL pointing to the filing document on SEC EDGAR.

        Returns
        -------
        str
            Cleaned plain-text content of the filing.
        """
        # TODO: implement — fetch the document, strip SGML/HTML tags,
        # handle encoding, and return clean text.
        raise NotImplementedError


class NewsAPIScraper:
    """Wrapper for financial news API (NewsAPI, GDELT, etc.).

    Parameters
    ----------
    api_key : str
        API key for the news provider.
    provider : str
        News API provider name. Defaults to ``"newsapi"``.
    """

    def __init__(self, api_key: str, provider: str = "newsapi") -> None:
        # TODO: implement — store credentials and initialise the
        # appropriate API client based on the provider.
        self.api_key = api_key
        self.provider = provider

    def fetch_articles(
        self,
        query: str,
        from_date: str,
        to_date: str,
        *,
        language: str = "en",
        max_results: int = 100,
    ) -> list[dict]:
        """Fetch news articles matching a query within a date range.

        Parameters
        ----------
        query : str
            Search query (keywords, ticker symbols, etc.).
        from_date : str
            Start date (``YYYY-MM-DD``).
        to_date : str
            End date (``YYYY-MM-DD``).
        language : str
            Language filter. Defaults to ``"en"``.
        max_results : int
            Maximum number of articles to return.

        Returns
        -------
        list[dict]
            List of article dicts with keys: ``"title"``, ``"source"``,
            ``"published_at"``, ``"url"``, ``"content"``, ``"description"``.
        """
        # TODO: implement — call the appropriate provider API, handle
        # pagination and rate limits, and return normalised results.
        raise NotImplementedError


class EarningsCallScraper:
    """Earnings call transcript retrieval.

    Parameters
    ----------
    provider : str
        Transcript data provider name (e.g. ``"seeking_alpha"``,
        ``"fool"``, ``"custom"``).
    """

    def __init__(self, provider: str) -> None:
        # TODO: implement — initialise scraping session for the given
        # provider with appropriate authentication.
        self.provider = provider

    def get_transcript(self, ticker: str, quarter: str, year: int) -> dict:
        """Retrieve a single earnings call transcript.

        Parameters
        ----------
        ticker : str
            Company ticker symbol.
        quarter : str
            Fiscal quarter (e.g. ``"Q1"``, ``"Q2"``).
        year : int
            Fiscal year.

        Returns
        -------
        dict
            Transcript data with keys: ``"ticker"``, ``"quarter"``,
            ``"year"``, ``"date"``, ``"participants"``,
            ``"prepared_remarks"``, ``"qa_section"``, ``"full_text"``.
        """
        # TODO: implement — fetch the transcript from the provider,
        # parse prepared remarks vs. Q&A sections, and return
        # structured output.
        raise NotImplementedError


class RedditScraper:
    """Reddit (PRAW) wrapper for financial subreddits.

    Parameters
    ----------
    client_id : str
        Reddit API OAuth client ID.
    client_secret : str
        Reddit API OAuth client secret.
    user_agent : str
        User-agent string for the Reddit API.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        user_agent: str,
    ) -> None:
        # TODO: implement — initialise PRAW Reddit client with the
        # given credentials and verify connectivity.
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent

    def fetch_posts(
        self,
        subreddit: str,
        limit: int = 100,
        *,
        sort: str = "new",
        time_filter: str = "week",
    ) -> list[dict]:
        """Fetch posts from a financial subreddit.

        Parameters
        ----------
        subreddit : str
            Name of the subreddit (e.g. ``"wallstreetbets"``).
        limit : int
            Maximum number of posts to return.
        sort : str
            Sort order (``"new"``, ``"hot"``, ``"top"``, ``"rising"``).
        time_filter : str
            Time filter for ``"top"`` sort (``"day"``, ``"week"``,
            ``"month"``, ``"year"``, ``"all"``).

        Returns
        -------
        list[dict]
            List of post dicts with keys: ``"id"``, ``"title"``,
            ``"selftext"``, ``"author"``, ``"created_utc"``, ``"score"``,
            ``"num_comments"``, ``"url"``, ``"subreddit"``.
        """
        # TODO: implement — use PRAW to fetch posts, extract relevant
        # fields, handle deleted/removed posts, and filter out non-text
        # submissions.
        raise NotImplementedError


class CentralBankScraper:
    """Central bank communications (Fed, ECB, BoJ).

    Parameters
    ----------
    institution : str
        Central bank identifier (``"fed"``, ``"ecb"``, ``"boj"``).
        Defaults to ``"fed"``.
    """

    def __init__(self, institution: str = "fed") -> None:
        # TODO: implement — configure the scraper for the target
        # central bank's website structure and URL patterns.
        self.institution = institution

    def get_statements(
        self,
        start_date: str,
        end_date: str,
    ) -> list[dict]:
        """Retrieve policy statements within a date range.

        Parameters
        ----------
        start_date : str
            Start date (``YYYY-MM-DD``).
        end_date : str
            End date (``YYYY-MM-DD``).

        Returns
        -------
        list[dict]
            List of statement dicts with keys: ``"date"``, ``"title"``,
            ``"url"``, ``"text"``, ``"institution"``.
        """
        # TODO: implement — scrape or call the appropriate central bank
        # API/website to retrieve policy statements, parse and clean the
        # text content.
        raise NotImplementedError

    def get_minutes(
        self,
        start_date: str,
        end_date: str,
    ) -> list[dict]:
        """Retrieve meeting minutes within a date range.

        Parameters
        ----------
        start_date : str
            Start date (``YYYY-MM-DD``).
        end_date : str
            End date (``YYYY-MM-DD``).

        Returns
        -------
        list[dict]
            List of minutes dicts with keys: ``"date"``, ``"title"``,
            ``"url"``, ``"text"``, ``"institution"``.
        """
        # TODO: implement — scrape central bank meeting minutes pages,
        # download and parse PDF/HTML documents, extract clean text.
        raise NotImplementedError
