#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

from typing import Sequence

import msgspec
import sqlmodel
from sqlalchemy.engine.base import Engine
from sqlmodel import Session

from docs import domain
from . import _orm as orm


class Library:
    """A repository for Zotero libraries.

    This class provides methods to interact with the database for operations
    related to libraries.

    Attributes:
        engine: The SQLAlchemy engine object used for database operations.

    """

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def add(self, library: domain.Library) -> None:
        """Add a new library to the database."""
        with Session(self.engine) as session:
            session.add(orm.Library(**msgspec.to_builtins(library)))
            session.commit()

    def get(self, library_id: int) -> domain.Library | None:
        """Retrieve an instance of a library by id."""

        with Session(self.engine) as session:
            if (library := session.get(orm.Library, library_id)) is None:
                return None
            return domain.Library(library.model_dump())

    def list(self) -> Sequence[domain.Library]:
        """Retrieve all instances of a given class from the database."""
        with Session(self.engine) as session:
            return [
                domain.Library(library.model_dump())
                for library in session.exec(sqlmodel.select(orm.Library)).all()
            ]
