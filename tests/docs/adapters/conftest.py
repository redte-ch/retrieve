#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import pytest

import docs

# from zotero.adapters import orm


@pytest.fixture()
def db_path(tmp_path):
    return tmp_path / "sqlite.db"


@pytest.fixture
def db_engine(db_path):
    return docs.create_db_engine(db_path)


@pytest.fixture(autouse=True)
def create_db(db_engine):
    # orm.BaseORM.metadata.create_all(db_engine)
    return docs.create_db(db_engine)
