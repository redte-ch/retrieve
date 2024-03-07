#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import pytest

from docs.adapters.repo import LibraryRepo
from docs.domain import Library


@pytest.fixture
def repo(db_engine):
    return LibraryRepo(db_engine)


def test_add_a_library_to_the_database(repo):
    # Arrange
    library = Library()

    # Act
    repo.add(library)

    # Assert
    assert isinstance(repo.get(1), Library)


# @patch('sqlalchemy.orm.Session')
# def test_retrieving_library_by_id(mock_session):
#     mock_engine = Mock()
#     repo = LibraryRepo(mock_engine)
#     mock_library_id = 1
#
#     repo.get(mock_library_id)
#
#     mock_session.assert_called_once_with(mock_engine)
#     mock_session.return_value.__enter__.return_value.get.assert_called_once_with(Library, mock_library_id)
#
# @patch('sqlalchemy.orm.Session')
# def test_retrieving_all_libraries(mock_session):
#     mock_engine = Mock()
#     repo = LibraryRepo(mock_engine)
#
#     repo.list()
#
#     mock_session.assert_called_once_with(mock_engine)
#     mock_session.return_value.__enter__.return_value.query.assert_called_once_with(Library)
#     mock_session.return_value.__enter__.return_value.query.return_value.all.assert_called_once()
