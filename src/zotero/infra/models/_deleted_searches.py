#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import datetime
import decimal

from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    Table,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)
from sqlalchemy.sql.sqltypes import NullType

from ._base import Base


class DeletedSearches(SavedSearches):
    __tablename__ = "deletedSearches"

    dateDeleted: Mapped[Any] = mapped_column(
        NullType, server_default=text("CURRENT_TIMESTAMP")
    )
    savedSearchID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("savedSearches.savedSearchID", ondelete="CASCADE"), primary_key=True
    )
