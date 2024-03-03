import json

import pytest

from zotero_qa import Cache


@pytest.fixture()
def tmp_dir(tmp_path):
    sub_dir = tmp_path / "sub_dir"
    sub_dir.mkdir()
    return sub_dir


@pytest.fixture()
def cache(tmp_dir):
    cache_path = tmp_dir / "cache.json"
    cache_file = str(cache_path)
    return Cache(cache_file)


def test_cache_set(cache):
    # Arrange
    key = "pdf"
    value = 1

    # Act
    cache.set(key, value)
    result = cache.get(key)

    # Assert
    assert result == value


def test_cache_get_when_miss(cache):
    # Arrange
    key = "pdf"

    # Act
    result = cache.get(key)

    # Assert
    assert result == -1


def test_has_key(cache):
    # Arrange
    key = "key"

    # Act
    cache.set(key, 1)

    # Assert
    assert cache.has_key(key)


def test_has_key_when_miss(cache):
    # Arrange
    key = "key"

    # Assert
    assert not cache.has_key(key)


def test_load_cache_from_existing_file(tmp_dir):
    # Arrange
    cache_path = tmp_dir / "cache.json"
    cache_file = str(cache_path)
    dump = {"key": 1}

    with open(cache_file, "w") as f:
        json.dump(dump, f)

    # Act
    cache = Cache(cache_file)
    value = cache.get("key")

    # Assert
    assert value == 1
