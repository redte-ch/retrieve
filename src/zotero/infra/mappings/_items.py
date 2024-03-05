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

from sqlalchemy import (
    TIMESTAMP,
    ForeignKey,
    Index,
    Integer,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

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
    itemID: Mapped[int | None] = mapped_column(Integer, primary_key=True)

    libraries: Mapped["Libraries"] = relationship("Libraries", back_populates="items")
    fulltextWords: Mapped[list["FulltextWords"]] = relationship(
        "FulltextWords", secondary="fulltextItemWords", back_populates="items"
    )
    collectionItems: Mapped[list["CollectionItems"]] = relationship(
        "CollectionItems", back_populates="items"
    )
    itemAttachments: Mapped[list["ItemAttachments"]] = relationship(
        "ItemAttachments",
        foreign_keys="[ItemAttachments.parentItemID]",
        back_populates="items",
    )
    itemCreators: Mapped[list["ItemCreators"]] = relationship(
        "ItemCreators", back_populates="items"
    )
    itemData: Mapped[list["ItemData"]] = relationship(
        "ItemData", back_populates="items"
    )
    itemNotes: Mapped[list["ItemNotes"]] = relationship(
        "ItemNotes", foreign_keys="[ItemNotes.parentItemID]", back_populates="items"
    )
    itemRelations: Mapped[list["ItemRelations"]] = relationship(
        "ItemRelations", back_populates="items"
    )
    itemTags: Mapped[list["ItemTags"]] = relationship(
        "ItemTags", back_populates="items"
    )
