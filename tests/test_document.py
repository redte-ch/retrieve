from zotero_qa.document import Document


def test_document_initialization():
    # Arrange
    page_content = "The Tortoise is a famous paradox from the Greek..."
    metadata = {"page": "0", "source": "Zeno of Elea"}

    # Act
    doc = Document(page_content, metadata)

    # Assert
    assert doc.page_content == page_content
    assert doc.metadata == metadata
