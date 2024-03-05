#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import ForeignKey, Index, Integer, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._items import Items


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

    itemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    parentItemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE")
    )
    linkMode: Mapped[int | None] = mapped_column(Integer)
    contentType: Mapped[str | None] = mapped_column(Text)
    charsetID: Mapped[int | None] = mapped_column(
        ForeignKey("charsets.charsetID", ondelete="SET NULL")
    )
    path: Mapped[str | None] = mapped_column(Text)
    syncState: Mapped[int | None] = mapped_column(Integer, server_default=text("0"))
    storageModTime: Mapped[int | None] = mapped_column(Integer)
    storageHash: Mapped[str | None] = mapped_column(Text)
    lastProcessedModificationTime: Mapped[int | None] = mapped_column(Integer)

    charsets: Mapped["Charsets"] = relationship(
        "Charsets", back_populates="itemAttachments"
    )
    items: Mapped["Items"] = relationship(
        "Items", foreign_keys=[parentItemID], back_populates="itemAttachments"
    )
    itemAnnotations: Mapped[list["ItemAnnotations"]] = relationship(
        "ItemAnnotations", back_populates="itemAttachments"
    )
