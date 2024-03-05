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


class SyncCache(Base):
    __tablename__ = "syncCache"

    libraryID: Mapped[int] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE"), primary_key=True
    )
    key: Mapped[str] = mapped_column(Text, primary_key=True)
    syncObjectTypeID: Mapped[int] = mapped_column(
        ForeignKey("syncObjectTypes.syncObjectTypeID"), primary_key=True
    )
    version: Mapped[int] = mapped_column(Integer, primary_key=True)
    data: Mapped[Optional[str]] = mapped_column(Text)

    libraries: Mapped["Libraries"] = relationship(
        "Libraries", back_populates="syncCache"
    )
    syncObjectTypes: Mapped["SyncObjectTypes"] = relationship(
        "SyncObjectTypes", back_populates="syncCache"
    )
