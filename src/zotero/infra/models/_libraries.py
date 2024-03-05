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


class Libraries(Base):
    __tablename__ = "libraries"

    type: Mapped[str] = mapped_column(Text)
    editable: Mapped[int] = mapped_column(Integer)
    filesEditable: Mapped[int] = mapped_column(Integer)
    version: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    storageVersion: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    lastSync: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    archived: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    libraryID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)

    collections: Mapped[List["Collections"]] = relationship(
        "Collections", back_populates="libraries"
    )
    groups: Mapped["Groups"] = relationship(
        "Groups", uselist=False, back_populates="libraries"
    )
    items: Mapped[List["Items"]] = relationship("Items", back_populates="libraries")
    savedSearches: Mapped[List["SavedSearches"]] = relationship(
        "SavedSearches", back_populates="libraries"
    )
    storageDeleteLog: Mapped[List["StorageDeleteLog"]] = relationship(
        "StorageDeleteLog", back_populates="libraries"
    )
    syncCache: Mapped[List["SyncCache"]] = relationship(
        "SyncCache", back_populates="libraries"
    )
    syncQueue: Mapped[List["SyncQueue"]] = relationship(
        "SyncQueue", back_populates="libraries"
    )
    syncedSettings: Mapped[List["SyncedSettings"]] = relationship(
        "SyncedSettings", back_populates="libraries"
    )
