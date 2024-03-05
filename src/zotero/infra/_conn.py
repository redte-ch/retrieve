#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


def create_db_engine(db_path: str) -> Engine:
    """Create an SQLAlchemy database engine.

    Args:
        db_path (str): The path to the database.

    Returns:
        Engine: The SQLAlchemy database engine.

    """
    return create_engine(f"sqlite:///{db_path}")
