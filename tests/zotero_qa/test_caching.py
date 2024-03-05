#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import pytest

from zotero_qa import Cache


@pytest.fixture()
def tmp_dir(tmp_path):
    sub_dir = tmp_path / "test_dir"
    sub_dir.mkdir()
    return sub_dir


@pytest.fixture()
def cache(tmp_dir):
    temp_file = tmp_dir / "cache.bin"
    with open(temp_file, "wb") as f:
        f.write(b'{"key": {}}')
    return Cache(str(temp_file))


def test_cache_open_when_the_file_cache_does_not_exist(tmp_dir):
    # Arrange
    path = tmp_dir / "cache.bin"

    # Act
    cache = Cache(str(path))
    cache.load()

    # Assert
    assert cache.cache == {}


def test_cache_open_when_the_file_cache_exists(cache):
    # Act
    cache.load()

    # Assert
    assert cache.cache == {"key": {}}


def test_cache_save(cache):
    # Arrange
    value = {"key": {"pages": 2, "embedded": 0}}
    cache.cache = value

    # Act
    cache.save()
    cache = Cache(str(cache.path))

    # Assert
    cache.load()
    assert cache.cache == value


def test_cache_set(cache):
    # Arrange
    key = "pdf"
    value = {"anything": 0}

    # Act
    cache.set(key, value)
    result = cache.get(key)

    # Assert
    assert result == value
