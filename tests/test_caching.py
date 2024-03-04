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
    with open(temp_file, "w") as f:
        f.write('{"key": 1}')
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
    assert cache.cache == {"key": 1}


def test_cache_save(cache):
    # Arrange
    cache.cache = {"key": 2}

    # Act
    cache.save()
    cache = Cache(str(cache.path))

    # Assert
    cache.load()
    assert cache.cache == {"key": 2}


def test_cache_set(cache):
    # Arrange
    key = "pdf"
    value = 1

    # Act
    cache.set(key, value)
    result = cache.get(key)

    # Assert
    assert result == value
