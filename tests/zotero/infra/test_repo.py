#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


import pytest
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

import zotero
from zotero import Base, Repo


class TestClass(Base):
    __tablename__ = "tests"
    testID: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(30))


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
    instance = TestClass(type="test")

    # Act
    repo.add(instance)

    # Assert
    assert repo.all(TestClass)[-1].type == "test"


def test_update(repo):
    # Arrange
    repo.add(TestClass(type="test1"))
    testID = repo.all(TestClass)[-1].testID

    # Act
    repo.update(TestClass, testID, type="test2")

    # Assert
    assert repo.find(TestClass, testID).type == "test2"


def test_delete(repo):
    # Arrange
    repo.add(TestClass(type="test1"))
    instance = repo.all(TestClass)[-1]

    # Act
    repo.delete(instance)

    # Assert
    assert len(repo.all(TestClass)) == 0


def test_filter(repo):
    # Arrange
    repo.add(TestClass(type="test1"))
    repo.add(TestClass(type="test2"))

    # Act
    instances = repo.filter(TestClass, type="test1")

    # Assert
    assert len(list(instances)) == 1
