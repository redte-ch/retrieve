from pathlib import Path

from zotero_qa import PDFLoader


def test_load():
    # Arrange
    path = "tests/pdf/files/1mb.pdf"
    loader = PDFLoader(Path(path))

    # Act
    doc = loader.load()

    # Assert
    assert loader.file_path == path
    assert loader.source == path
    assert doc.page_count == 1


def test_load_with_images():
    # Arrange
    path = "tests/pdf/files/5mb-with-images.pdf"
    loader = PDFLoader(Path(path))

    # Act
    doc = loader.load()

    # Assert
    assert loader.file_path == path
    assert loader.source == path
    assert doc.page_count == 10


def test_load_big():
    # Arrange
    path = "tests/pdf/files/10mb.pdf"
    loader = PDFLoader(Path(path))

    # Act
    doc = loader.load()

    # Assert
    assert loader.file_path == path
    assert loader.source == path
    assert doc.page_count == 12


def test_load_big_with_images():
    # Arrange
    path = "tests/pdf/files/50mb-with-images.pdf"
    loader = PDFLoader(Path(path))

    # Act
    doc = loader.load()

    # Assert
    assert loader.file_path == path
    assert loader.source == path
    assert doc.page_count == 1
