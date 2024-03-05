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


class Items(Base):
    __tablename__ = "items"
    __table_args__ = (
        UniqueConstraint("libraryID", "key"),
        Index("items_synced", "synced"),
    )

    itemTypeID: Mapped[int] = mapped_column(Integer)
    dateAdded: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    dateModified: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    clientDateModified: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    libraryID: Mapped[int] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE")
    )
    key: Mapped[str] = mapped_column(Text)
    version: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    synced: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    itemID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)

    libraries: Mapped["Libraries"] = relationship("Libraries", back_populates="items")
    fulltextWords: Mapped[List["FulltextWords"]] = relationship(
        "FulltextWords", secondary="fulltextItemWords", back_populates="items"
    )
    collectionItems: Mapped[List["CollectionItems"]] = relationship(
        "CollectionItems", back_populates="items"
    )
    itemAttachments: Mapped[List["ItemAttachments"]] = relationship(
        "ItemAttachments",
        foreign_keys="[ItemAttachments.parentItemID]",
        back_populates="items",
    )
    itemCreators: Mapped[List["ItemCreators"]] = relationship(
        "ItemCreators", back_populates="items"
    )
    itemData: Mapped[List["ItemData"]] = relationship(
        "ItemData", back_populates="items"
    )
    itemNotes: Mapped[List["ItemNotes"]] = relationship(
        "ItemNotes", foreign_keys="[ItemNotes.parentItemID]", back_populates="items"
    )
    itemRelations: Mapped[List["ItemRelations"]] = relationship(
        "ItemRelations", back_populates="items"
    )
    itemTags: Mapped[List["ItemTags"]] = relationship(
        "ItemTags", back_populates="items"
    )
