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

t_fulltextItemWords = Table(
    "fulltextItemWords",
    Base.metadata,
    Column("wordID", ForeignKey("fulltextWords.wordID"), primary_key=True),
    Column("itemID", ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True),
    Index("fulltextItemWords_itemID", "itemID"),
)
