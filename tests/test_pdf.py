import pytest

from zotero_qa import DocLoader, PageParser


@pytest.fixture
def loader():
    path = "tests/files/1mb.pdf"
    return DocLoader(path)


@pytest.fixture
def parser(loader):
    return PageParser(loader)


def test_parse(parser):
    # Act
    page = parser.parse(1)
    text = page["text"]
    metadata = page["metadata"]

    # Assert
    assert text.startswith("Lorem Ipsum")
    assert "\n\n" in text
    assert metadata["author"] == "Dainik"
    assert metadata["created_at"] == "D:20190906105309+00'00'"
    assert metadata["creator"] == "Microsoft® Word 2016"
    assert metadata["format"] == "PDF 1.5"
    assert metadata["keywords"] == ""
    assert metadata["page"] == 1
    assert metadata["path"] == "tests/files/1mb.pdf"
    assert metadata["producer"] == "www.ilovepdf.com"
    assert metadata["subject"] == ""
    assert metadata["title"] == ""
    assert metadata["total_pages"] == 1
    assert metadata["updated_at"] == "D:20190906105310Z"
