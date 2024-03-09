#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


import pytest
import sqlalchemy
from sqlalchemy.orm import Session

from docs.domain import Collection
from docs.infra import Collections, Repo


@pytest.fixture
def repo(db_engine):
    return Repo(Collection, Collections, db_engine)


def test_add_a_collection_to_the_database(repo):
    # Act
    repo.add(Collection(name="Col1", collection_id=0, library_id=0, key="key"))
    repo.add(Collection(name="Col2", collection_id=0, library_id=0, key="key"))

    # Assert
    with Session(repo.engine) as session:
        statement = sqlalchemy.text("SELECT collectionName FROM collections ;")
        [[col1], [col2]] = session.execute(statement).all()
        assert [col1, col2] == ["Col1", "Col2"]


def test_get_a_collection_from_the_database(repo):
    # Act
    with Session(repo.engine) as session:
        statement = sqlalchemy.text(
            "INSERT INTO collections "
            "(collectionName, parentCollectionID, libraryID, key) "
            'VALUES ("Col1", 0, 0, "key") ;'
        )
        session.execute(statement)
        session.commit()

    # Assert
    collection = repo.get(1)
    assert collection.name == "Col1"


def test_get_all_libraries_from_the_database(repo):
    # Act
    with Session(repo.engine) as session:
        statement = sqlalchemy.text(
            "INSERT INTO collections "
            "(collectionName, parentCollectionID, libraryID, key) "
            'SELECT "Col1", 0, 0, "key" UNION ALL '
            'SELECT "Col2", 0, 0, "key" ;'
        )
        session.execute(statement)
        session.commit()

    # Assert
    collections = repo.list()
    assert [collection.name for collection in collections] == ["Col1", "Col2"]
