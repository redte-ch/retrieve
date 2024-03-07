#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

import pathlib

from sqlalchemy.engine.base import Engine
from sqlmodel import SQLModel, create_engine


def create_db_engine(db_path: pathlib.Path | str) -> Engine:
    """Create an SQLAlchemy database engine."""
    return create_engine(f"sqlite:///{db_path}")


def create_db(engine: Engine) -> None:
    """Create the database."""
    SQLModel.metadata.create_all(engine)
