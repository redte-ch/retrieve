import zotero_qa


def test_load_files():
    # Arrange
    path = "tests/files"

    # Act
    files = zotero_qa.list_files(path)

    # Assert
    assert len(files) == 4
    assert "1mb.pdf" in str(files[0])


def test_open_file():
    # Arrange
    path = "tests/files/10mb.pdf"

    # Act
    pages = zotero_qa.open_file(path)

    # Assert
    assert len(pages) == 9
