#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import ForeignKey, Index, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._items import Items


class ItemAnnotations(Items):
    __tablename__ = "itemAnnotations"
    __table_args__ = (Index("itemAnnotations_parentItemID", "parentItemID"),)

    parentItemID: Mapped[int] = mapped_column(ForeignKey("itemAttachments.itemID"))
    type: Mapped[int] = mapped_column(Integer)
    sortIndex: Mapped[str] = mapped_column(Text)
    position: Mapped[str] = mapped_column(Text)
    isExternal: Mapped[int] = mapped_column(Integer)
    itemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    authorName: Mapped[str | None] = mapped_column(Text)
    text_: Mapped[str | None] = mapped_column("text", Text)
    comment: Mapped[str | None] = mapped_column(Text)
    color: Mapped[str | None] = mapped_column(Text)
    pageLabel: Mapped[str | None] = mapped_column(Text)

    itemAttachments: Mapped["ItemAttachments"] = relationship(
        "ItemAttachments", back_populates="itemAnnotations"
    )
