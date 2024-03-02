import pytest

from zotero_qa.text_splitter import TextSplitter


@pytest.fixture()
def splitter():
    return TextSplitter(chunk_size=2, chunk_overlap=1, separator = "\t\t")


def test_split_text(splitter):
    # Arrange
    separator = splitter.separator_pattern
    text = f"This\t\tis a\n\ntest text.\n\n Don't\n\ntry this\n\nhome."

    # Act
    chunks = splitter.split_text(text)

    # Assert
    assert len(chunks) == 2


# def test_split_text_with_overlap():
#     splitter = TextSplitter(chunk_size=10, chunk_overlap=2)
#     text = "12345 67890 12345 67890"
#     # Expect overlap; the '67890' part should be repeated because of the overlap setting
#     expected = ["12345 67890", "67890 12345", "12345 67890"]
#     assert splitter.split_text(text) == expected, "Should respect the chunk overlap setting."
#
# def test_split_documents():
#     splitter = TextSplitter(chunk_size=10, chunk_overlap=0)
#     docs = [Document(page_content="First document content.", metadata={"id": 1}),
#             Document(page_content="Second document content longer than chunk size.", metadata={"id": 2})]
#     result_docs = splitter.split_documents(docs)
#
#     assert len(result_docs) == 4, "Should split documents into correct number of chunks."
#     # Further checks can include verifying the content of each chunk and its metadata
#
# def test_empty_text():
#     splitter = TextSplitter(chunk_size=10, chunk_overlap=0)
#     assert splitter.split_text("") == [], "Should return an empty list for empty text."
