#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from typing import Any, Type, TypeVar

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Query, Session

T = TypeVar("T")


class Repo:
    def __init__(self, engine: Engine) -> None:
        """Initializes the Repo class with a session object.

        Args:
            engine: The engine object to be used for database operations.

        """

        self.engine = engine

    def all(self, cls: Type[T]) -> list[T]:
        """Retrieves all instances of a given class from the database.

        Args:
            cls: The class to retrieve instances of.

        Returns:
            List of all instances of the given class.

        """

        with Session(self.engine) as s:
            return s.query(cls).all()

    def find(self, cls: Type[T], id: int) -> T | None:
        """Retrieves an instance of a given class by its ID from the database.

        Args:
            cls: The class of the instance to retrieve.
            id: The ID of the instance to retrieve.

        Returns:
            The instance with the given ID.

        """

        with Session(self.engine) as s:
            return s.get(cls, id)

    def filter(self, cls: Type[T], **kwargs: Any) -> Query[T]:
        """Filters instances of a given class based on the provided criteria.

        Args:
            cls: The class to filter instances of.
            **kwargs: Filtering criteria in the form of key-value pairs.

        Returns:
            Filtered instances of the given class.

        """

        with Session(self.engine) as s:
            return s.query(cls).filter_by(**kwargs)

    def add(self, item: T) -> None:
        """Adds a new item to the database.

        Args:
            item: The item to be added to the database.

        """

        with Session(self.engine) as s:
            s.add(item)
            s.commit()

    def update(self, cls: Type[T], id: int, **kwargs: Any) -> None:
        """Updates an item in the database based on the provided criteria.

        Args:
            cls: The class of the item to update.
            id: The ID of the item to update.
            **kwargs: Update criteria in the form of key-value pairs.

        """

        with Session(self.engine) as s:
            item = s.get(cls, id)
            for k, v in kwargs.items():
                setattr(item, k, v)
            s.commit()

    def delete(self, item: T) -> None:
        """
        Deletes an item from the database.

        Args:
            item: The item to be deleted from the database.

        """

        with Session(self.engine) as s:
            s.delete(item)
            s.commit()
