#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

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
