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


class Collections(Base):
    __tablename__ = "collections"
    __table_args__ = (
        UniqueConstraint("libraryID", "key"),
        Index("collections_synced", "synced"),
    )

    collectionName: Mapped[str] = mapped_column(Text)
    clientDateModified: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    libraryID: Mapped[int] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE")
    )
    key: Mapped[str] = mapped_column(Text)
    version: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    synced: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    collectionID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    parentCollectionID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("collections.collectionID", ondelete="CASCADE"),
        server_default=text("NULL"),
    )

    libraries: Mapped["Libraries"] = relationship(
        "Libraries", back_populates="collections"
    )
    collections: Mapped["Collections"] = relationship(
        "Collections", remote_side=[collectionID], back_populates="collections_reverse"
    )
    collections_reverse: Mapped[List["Collections"]] = relationship(
        "Collections", remote_side=[parentCollectionID], back_populates="collections"
    )
    collectionItems: Mapped[List["CollectionItems"]] = relationship(
        "CollectionItems", back_populates="collections"
    )
    collectionRelations: Mapped[List["CollectionRelations"]] = relationship(
        "CollectionRelations", back_populates="collections"
    )
