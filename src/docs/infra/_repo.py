#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

from typing import Sequence

import sqlmodel
from sqlalchemy.engine.base import Engine
from sqlmodel import Session

from docs.typing import ORM, Model


class Repo:
    """A repository for Zotero models.

    Attributes:
        engine: The SQLAlchemy engine object used for database operations.

    """

    def __init__(
        self,
        model: type[Model],
        orm: type[ORM],
        engine: Engine,
    ) -> None:
        self.engine = engine
        self.Model = model
        self.ORM = orm

    def add(self, model: Model) -> None:
        """Add a new library to the database."""
        with Session(self.engine) as session:
            session.add(self.ORM.from_model(model))
            session.commit()

    def get(self, model_id: int) -> Model | None:
        """Retrieve an instance of a library by id."""
        with Session(self.engine) as session:
            model = session.get(self.ORM, model_id)
            return model.to_model() if model is not None else None

    def list(self) -> Sequence[Model]:
        """Retrieve all instances of a given class from the database."""
        with Session(self.engine) as session:
            return [
                model.to_model()
                for model in session.exec(sqlmodel.select(self.ORM)).all()
            ]
