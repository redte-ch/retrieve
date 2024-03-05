#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import pytest

import zotero
from zotero import Base, Item, Repo


@pytest.fixture()
def tmp_dir(tmp_path):
    sub_dir = tmp_path / "test_dir"
    sub_dir.mkdir()
    return sub_dir


@pytest.fixture()
def tmp_db_path(tmp_dir):
    return tmp_dir / "sqlite.db"


@pytest.fixture
def db_engine(tmp_db_path):
    return zotero.create_db_engine(tmp_db_path)


@pytest.fixture
def repo(db_engine):
    return Repo(db_engine)


@pytest.fixture(autouse=True)
def create_db(db_engine):
    Base.metadata.create_all(db_engine)


def test_add(repo):
    # Arrange
    instance = Item(itemTypeID=1, libraryID=1, key="test")

    # Act
    repo.add(instance)

    # Assert
    assert repo.all(Item)[-1].key == "test"
