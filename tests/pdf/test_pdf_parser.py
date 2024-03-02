from pathlib import Path

import pytest

from zotero_qa import PDFLoader, PDFParser


@pytest.fixture
def loader():
    path = "tests/pdf/files/1mb.pdf"
    return PDFLoader(Path(path))


@pytest.fixture
def parser(loader):
    return PDFParser(loader)


def test_parse(parser):
    # Arrange
    docs = parser.parse()

    # Act
    page = next(docs)
    text = page["text"]
    metadata = page["metadata"]

    # Assert
    assert text.startswith("Lorem Ipsum")
    assert "\n\n" in text
    assert metadata["author"] == "Dainik"
    assert metadata["creationDate"] == "D:20190906105309+00'00'"
    assert metadata["creator"] == "Microsoft® Word 2016"
    assert metadata["file_path"] == "tests/pdf/files/1mb.pdf"
    assert metadata["format"] == "PDF 1.5"
    assert metadata["keywords"] == ""
    assert metadata["modDate"] == "D:20190906105310Z"
    assert metadata["page"] == 0
    assert metadata["producer"] == "www.ilovepdf.com"
    assert metadata["source"] == "tests/pdf/files/1mb.pdf"
    assert metadata["subject"] == ""
    assert metadata["title"] == ""
    assert metadata["total_pages"] == 1
