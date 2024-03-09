#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import pytest

from docs import app
from docs.domain import File, Item, Library
from docs.infra import ItemAttachments, Items, Libraries, Repo


@pytest.fixture()
def library_repo(db_engine):
    return Repo(Library, Libraries, db_engine)


@pytest.fixture()
def item_repo(db_engine):
    return Repo(Item, Items, db_engine)


@pytest.fixture()
def file_repo(db_engine):
    return Repo(File, ItemAttachments, db_engine)


@pytest.fixture()
def library(library_repo):
    library_repo.add(Library(type="user"))
    return library_repo.get(1)


@pytest.fixture()
def item(item_repo, library):
    item_repo.add(Item(type_id=0, library_id=library.id, key="NTQEM58T"))
    return item_repo.get(1)


def test_get_pdf_paths(item_repo, file_repo, item):
    # Arrange
    file_repo.add(
        File(
            id=item.id,
            link_mode=0,
            path="storage:1mb.pdf",
            content_type="application/pdf",
        )
    )
    # file_repo.add(
    #     File(
    #         link_mode=0,
    #         path="storage:10mb.pdf",
    #         content_type="application/pdf",
    #     )
    # )

    # Act
    pfd_paths = app.get_pdf_paths("./tests/data", item_repo)

    # Assert
    assert pfd_paths == ["./tests/data/storage/NTQEM58T/1mb.pdf"]
