#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


import pytest
import sqlalchemy
from sqlalchemy.orm import Session

from docs.domain import File
from docs.infra import ItemAttachments, Repo


@pytest.fixture
def repo(db_engine):
    return Repo(File, ItemAttachments, db_engine)


def test_add_a_file_to_the_database(repo):
    # Act
    repo.add(
        File(
            id=1,
            link_mode=0,
            path="file1.txt",
            content_type="text/plain",
            storage_hash="hash1",
        )
    )
    repo.add(
        File(
            id=2,
            link_mode=0,
            content_type="text/plain",
            path="file2.txt",
            storage_hash="hash2",
        )
    )

    # Assert
    with Session(repo.engine) as session:
        statement = sqlalchemy.text("SELECT path FROM itemAttachments ;")
        [[path1], [path2]] = session.execute(statement).all()
        assert [path1, path2] == ["file1.txt", "file2.txt"]


def test_get_a_file_from_the_database(repo):
    # Act
    with Session(repo.engine) as session:
        statement = sqlalchemy.text(
            "INSERT INTO itemAttachments "
            "(itemID, linkMode, contentType, path, storageHash) "
            'VALUES (1, 0, "pdf", "file1.pdf", "hash1") ;'
        )
        session.execute(statement)
        session.commit()

    # Assert
    file = repo.get(1)
    assert file.path == "file1.pdf"


def test_get_all_files_from_the_database(repo):
    # Act
    with Session(repo.engine) as session:
        statement = sqlalchemy.text(
            "INSERT INTO itemAttachments "
            "(itemID, linkMode, contentType, path, storageHash) "
            'SELECT 1, 0, "pdf", "file1.pdf", "hash1" UNION ALL '
            'SELECT 2, 0, "pdf", "file2.pdf", "hash2" ;'
        )
        session.execute(statement)
        session.commit()

    # Assert
    files = repo.list()
    assert [file.path for file in files] == ["file1.pdf", "file2.pdf"]
