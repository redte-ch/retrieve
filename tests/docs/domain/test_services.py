#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from docs import domain
from docs.domain import Item, File

import pytest

@pytest.fixture
def files():
    return [File(
        id=1,
        path="storage:1mb.pdf",
        contentType="application/pdf",
    )]

@pytest.fixture
def items(files):
    return [Item(
        key="NTQEM58T",
        files=files
    )]


def test_get_pdf_paths(items):
    # Act
    pfd_paths = domain.get_pdf_paths(items, "./tests/data")

    # Assert
    assert pfd_paths == ["./tests/data/storage/NTQEM58T/1mb.pdf"]


def test_get_pdf_paths_with_files_without_id(items):
    # Arrange
    object.__setattr__(items[0].files[0], "id", None)

    # Act
    pfd_paths = domain.get_pdf_paths(items, "./tests/data")

    # Assert
    assert pfd_paths == []
