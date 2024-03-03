import pytest

from zotero_qa import DocLoader, DocSplitter, PageParser, TextSplitter


@pytest.fixture()
def doc_splitter():
    return DocSplitter(chunk_size=0, chunk_overlap=0, separator="\n\n")


@pytest.fixture()
def doc_loader():
    path = "tests/files/1mb.pdf"
    return DocLoader(path)


@pytest.fixture()
def page_parser(doc_loader):
    return PageParser(doc_loader)


@pytest.fixture()
def text_splitter():
    return TextSplitter(chunk_size=0, chunk_overlap=0, separator="\n\n")


@pytest.fixture()
def text():
    return "This\t\tis a\n\ntest text.\n\n Don't\n\ntry this\n\nhome."


def test_split_doc(doc_splitter, page_parser):
    # Arrange
    total_pages = page_parser.doc.page_count

    # Act
    split_pages = doc_splitter.split(page_parser)

    # Assert
    assert len(split_pages) > total_pages


def test_split_text(text_splitter, text):
    # Act
    splits = text_splitter.split(text)

    # Assert
    assert len(splits) == 5


def test_merge_text(text_splitter, text):
    # Arrange
    splits = text_splitter.split(text)

    # Act
    merged = text_splitter.merge(splits)

    # Assert
    assert len(merged) - len(splits) == 0


def test_merge_text_with_chunks(text_splitter, text):
    # Arrange
    text_splitter.chunk_size = 15
    splits = text_splitter.split(text)

    # Act
    merged = text_splitter.merge(splits)

    # Assert
    assert len(merged) - len(splits) < 0


def test_merge_text_with_overlap(text_splitter, text):
    # Arrange
    text_splitter.chunk_overlap = 1
    splits = text_splitter.split(text)

    # Act
    merged = text_splitter.merge(splits)

    # Assert
    assert merged[0] == splits[0]
    assert merged[1] != splits[1]


def test_merge_text_with_chunks_and_overlap(text_splitter, text):
    # Arrange
    text_splitter.chunk_size = 25
    text_splitter.chunk_overlap = 1
    splits = text_splitter.split(text)

    # Act
    merged = text_splitter.merge(splits)

    # Assert
    assert merged[0] != splits[0]
    assert merged[1] != splits[1]
