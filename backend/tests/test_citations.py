import pytest

from backend.services.citations import (
    check_citations,
    extract_urls,
    normalize_url,
    unverified_links_note,
)


def test_extract_urls_strips_markdown_and_punctuation():
    text = "See [paper](https://arxiv.org/abs/1706.03762), and https://github.com/a/b."

    assert extract_urls(text) == [
        "https://arxiv.org/abs/1706.03762",
        "https://github.com/a/b",
    ]


def test_extract_urls_keeps_balanced_parentheses_and_dedupes():
    url = "https://en.wikipedia.org/wiki/BERT_(language_model)"

    assert extract_urls(f"{url} and again ({url})") == [url]


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("http://arxiv.org/pdf/2005.11401v4", "https://arxiv.org/abs/2005.11401"),
        ("https://arxiv.org/pdf/2005.11401.pdf", "https://arxiv.org/abs/2005.11401v2"),
        ("https://www.github.com/HuggingFace/PEFT/", "https://github.com/huggingface/peft"),
        ("https://github.com/a/b.git", "https://github.com/a/b"),
    ],
)
def test_equivalent_urls_normalize_identically(a, b):
    assert normalize_url(a) == normalize_url(b)


@pytest.mark.parametrize(
    ("a", "b"),
    [
        ("https://arxiv.org/abs/2005.11401", "https://arxiv.org/abs/2005.11402"),
        ("https://github.com/a/b", "https://github.com/a/b/blob/main/x.py"),
        ("https://site.dev/p?id=1", "https://site.dev/p?id=2"),
    ],
)
def test_different_resources_stay_distinct(a, b):
    assert normalize_url(a) != normalize_url(b)


def test_report_separates_grounded_and_ungrounded():
    sources = '{"url": "https://github.com/huggingface/peft"}'
    answer = "Use https://github.com/huggingface/peft or https://github.com/fake/repo"

    report = check_citations(answer, sources)

    assert report.grounded == ["https://github.com/huggingface/peft"]
    assert report.ungrounded == ["https://github.com/fake/repo"]
    assert report.grounding_rate == 0.5
    assert not report.is_grounded


def test_answer_without_links_is_grounded():
    report = check_citations("No good results found.", "")

    assert report.is_grounded
    assert report.grounding_rate == 1.0


def test_note_lists_every_unverified_link():
    report = check_citations("https://x.dev/a https://x.dev/b", "")

    note = unverified_links_note(report)

    assert "https://x.dev/a" in note and "https://x.dev/b" in note
