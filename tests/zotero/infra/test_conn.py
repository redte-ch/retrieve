#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import pytest

import zotero


@pytest.fixture()
def tmp_dir(tmp_path):
    sub_dir = tmp_path / "test_dir"
    sub_dir.mkdir()
    return sub_dir


@pytest.fixture()
def tmp_db_path(tmp_dir):
    return tmp_dir / "sqlite.db"


def test_create_db_engine(tmp_db_path):
    # Act
    engine = zotero.create_db_engine(tmp_db_path)

    # Assert
    assert engine is not None
