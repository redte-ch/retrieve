#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


import pytest
import sqlalchemy
from sqlalchemy.orm import Session

from docs.domain import Item
from docs.infra import Items, Repo


@pytest.fixture
def repo(db_engine):
    return Repo(Item, Items, db_engine)


def test_add_a_item_to_the_database(repo):
    # Act
    repo.add(Item(type_id=0, library_id=0, key="key1"))
    repo.add(Item(type_id=0, library_id=0, key="key2"))

    # Assert
    with Session(repo.engine) as session:
        statement = sqlalchemy.text("SELECT key FROM items ;")
        [[key1], [key2]] = session.execute(statement).all()
        assert [key1, key2] == ["key1", "key2"]


def test_get_a_item_from_the_database(repo):
    # Act
    with Session(repo.engine) as session:
        statement = sqlalchemy.text(
            "INSERT INTO items "
            "(itemTypeID, libraryID, key) "
            'VALUES (0, 0, "key") ;'
        )
        session.execute(statement)
        session.commit()

    # Assert
    item = repo.get(1)
    assert item.key == "key"


def test_get_all_libraries_from_the_database(repo):
    # Act
    with Session(repo.engine) as session:
        statement = sqlalchemy.text(
            "INSERT INTO items "
            "(itemTYpeID, libraryID, key) "
            'SELECT 0, 0, "key1" UNION ALL '
            'SELECT 0, 0, "key2" ;'
        )
        session.execute(statement)
        session.commit()

    # Assert
    items = repo.list()
    assert [item.key for item in items] == ["key1", "key2"]
