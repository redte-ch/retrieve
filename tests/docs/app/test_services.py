#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import pytest

from docs import app
from docs.domain import File, Item, Library
from docs.typing import Model


class TestRepo:
    def __init__(self, items: tuple[Model, ...] = ()) -> None:
        self._items = set(items)

    def add(self, item: Model) -> None:
        object.__setattr__(item, "id", len(self._items) + 1)
        self._items.add(item)

    def get(self, item_id: int) -> Model:
        return next((item for item in self._items if item.id == item_id), None)

    def list(self) -> tuple[Model, ...]:
        return tuple(self._items)


@pytest.fixture()
def library_repo(db_engine):
    return TestRepo()


@pytest.fixture()
def item_repo(db_engine):
    return TestRepo()


@pytest.fixture()
def file_repo(db_engine):
    return TestRepo()


@pytest.fixture()
def library(library_repo):
    library_repo.add(Library(type="user"))
    return library_repo.get(1)


@pytest.fixture()
def files(file_repo):
    file_repo.add(
        File(
            link_mode=0,
            path="storage:1mb.pdf",
            content_type="application/pdf",
        )
    )
    file_repo.add(
        File(
            link_mode=0,
            path="storage:10mb.pdf",
            content_type="application/pdf",
        )
    )
    return file_repo.list()


@pytest.fixture(autouse=True)
def create_item(item_repo, library, files):
    item_repo.add(Item(type_id=0, library_id=library.id, key="NTQEM58T", files=files))


def test_get_pdf_paths(item_repo):
    # Arrange
    for file in item_repo.get(1).files:
        if file.path == "storage:1mb.pdf":
            object.__setattr__(file, "id", None)

    # Act
    pfd_paths = app.get_pdf_paths("./tests/data", item_repo)

    # Assert
    assert pfd_paths == ["./tests/data/storage/NTQEM58T/10mb.pdf"]
