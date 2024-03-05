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


class Feeds(Libraries):
    __tablename__ = "feeds"

    name: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(Text, unique=True)
    libraryID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE"), primary_key=True
    )
    lastUpdate: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    lastCheck: Mapped[Optional[datetime.datetime]] = mapped_column(TIMESTAMP)
    lastCheckError: Mapped[Optional[str]] = mapped_column(Text)
    cleanupReadAfter: Mapped[Optional[int]] = mapped_column(Integer)
    cleanupUnreadAfter: Mapped[Optional[int]] = mapped_column(Integer)
    refreshInterval: Mapped[Optional[int]] = mapped_column(Integer)
