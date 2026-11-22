"""
Citation grounding check.

The system prompt tells the model to cite only papers and repositories that
the tools returned. This module verifies that mechanically: every URL in the
final answer must match a URL that appeared in the tool observations.

URLs are normalized before comparison so harmless variations still match:
    https://arxiv.org/pdf/2005.11401v4.pdf  ==  http://arxiv.org/abs/2005.11401
    https://www.GitHub.com/Org/Repo/        ==  https://github.com/org/repo
"""

import re
from dataclasses import dataclass, field
from urllib.parse import urlsplit

_URL_RE = re.compile(r"https?://[^\s<>\"'`\]]+", re.IGNORECASE)
_TRAILING = ".,;:!?*_"
_ARXIV_ID_RE = re.compile(
    r"^/(?:abs|pdf|html)/(?P<id>\d{4}\.\d{4,5}|[a-z\-]+(?:\.[a-z]{2})?/\d{7})(?:v\d+)?(?:\.pdf)?/?$",
    re.IGNORECASE,
)


def _strip_trailing(url: str) -> str:
    """Remove punctuation that belongs to the surrounding prose or Markdown."""
    while url:
        if url[-1] in _TRAILING:
            url = url[:-1]
        elif url[-1] == ")" and url.count("(") < url.count(")"):
            url = url[:-1]  # closing paren of a Markdown link, not part of the URL
        else:
            break
    return url


def extract_urls(text: str) -> list[str]:
    """All http(s) URLs in text, in order of appearance, without duplicates."""
    seen: dict[str, None] = {}
    for match in _URL_RE.findall(text or ""):
        url = _strip_trailing(match)
        if url:
            seen.setdefault(url, None)
    return list(seen)


def normalize_url(url: str) -> str:
    """Canonical form used to decide whether two URLs point to the same thing."""
    parts = urlsplit(url.strip())
    host = parts.netloc.lower().removeprefix("www.")
    path = parts.path.rstrip("/")

    if host in {"arxiv.org", "export.arxiv.org"}:
        match = _ARXIV_ID_RE.match(parts.path)
        if match:
            return f"arxiv:{match.group('id').lower()}"

    if host == "github.com":
        # Owner and repo names are case-insensitive on GitHub.
        path = path.lower().removesuffix(".git")

    query = f"?{parts.query}" if parts.query else ""
    return f"{host}{path}{query}"


@dataclass
class CitationReport:
    cited: list[str] = field(default_factory=list)
    grounded: list[str] = field(default_factory=list)
    ungrounded: list[str] = field(default_factory=list)

    @property
    def is_grounded(self) -> bool:
        return not self.ungrounded

    @property
    def grounding_rate(self) -> float:
        """Fraction of cited URLs backed by a tool result (1.0 if none cited)."""
        return len(self.grounded) / len(self.cited) if self.cited else 1.0


def check_citations(answer: str, sources: str) -> CitationReport:
    """
    Compare URLs cited in `answer` against URLs present in `sources`
    (the concatenated tool observations).
    """
    allowed = {normalize_url(url) for url in extract_urls(sources)}
    report = CitationReport()

    for url in extract_urls(answer):
        report.cited.append(url)
        if normalize_url(url) in allowed:
            report.grounded.append(url)
        else:
            report.ungrounded.append(url)

    return report


def unverified_links_note(report: CitationReport) -> str:
    """Markdown warning appended to answers that cite links no tool returned."""
    links = "\n".join(f"> - {url}" for url in report.ungrounded)
    return (
        "\n\n> **Unverified links:** the following were not returned by any "
        "search tool and may be inaccurate:\n" + links
    )
