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


class ItemAttachments(Items):
    __tablename__ = "itemAttachments"
    __table_args__ = (
        Index("itemAttachments_charsetID", "charsetID"),
        Index("itemAttachments_contentType", "contentType"),
        Index(
            "itemAttachments_lastProcessedModificationTime",
            "lastProcessedModificationTime",
        ),
        Index("itemAttachments_parentItemID", "parentItemID"),
        Index("itemAttachments_syncState", "syncState"),
    )

    itemID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    parentItemID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE")
    )
    linkMode: Mapped[Optional[int]] = mapped_column(Integer)
    contentType: Mapped[Optional[str]] = mapped_column(Text)
    charsetID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("charsets.charsetID", ondelete="SET NULL")
    )
    path: Mapped[Optional[str]] = mapped_column(Text)
    syncState: Mapped[Optional[int]] = mapped_column(Integer, server_default=text("0"))
    storageModTime: Mapped[Optional[int]] = mapped_column(Integer)
    storageHash: Mapped[Optional[str]] = mapped_column(Text)
    lastProcessedModificationTime: Mapped[Optional[int]] = mapped_column(Integer)

    charsets: Mapped["Charsets"] = relationship(
        "Charsets", back_populates="itemAttachments"
    )
    items: Mapped["Items"] = relationship(
        "Items", foreign_keys=[parentItemID], back_populates="itemAttachments"
    )
    itemAnnotations: Mapped[List["ItemAnnotations"]] = relationship(
        "ItemAnnotations", back_populates="itemAttachments"
    )
