#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import pytest
import sqlalchemy
from sqlalchemy.orm import Session

from docs.domain import Library
from docs.infra import Libraries, Repo


@pytest.fixture
def repo(db_engine):
    return Repo(Library, Libraries, db_engine)


def test_add_a_library_to_the_database(repo):
    # Act
    repo.add(Library(type="user"))
    repo.add(Library(type="group"))

    # Assert
    with Session(repo.engine) as session:
        statement = sqlalchemy.text("SELECT type FROM libraries ;")
        [[user], [group]] = session.execute(statement).all()
        assert [user, group] == ["user", "group"]


def test_get_a_library_from_the_database(repo):
    # Act
    with Session(repo.engine) as session:
        statement = sqlalchemy.text(
            "INSERT INTO libraries (type, editable, filesEditable) "
            'VALUES ("group", 0, 1) ;'
        )
        session.execute(statement)
        session.commit()

    # Assert
    library = repo.get(1)
    assert library.type == "group"


def test_get_all_libraries_from_the_database(repo):
    # Act
    with Session(repo.engine) as session:
        statement = sqlalchemy.text(
            "INSERT INTO libraries (type, editable, filesEditable) "
            'SELECT "user", 0, 1 UNION ALL '
            'SELECT "group", 1, 0 ;'
        )
        session.execute(statement)
        session.commit()

    # Assert
    libraries = repo.list()
    assert [library.type for library in libraries] == ["user", "group"]
