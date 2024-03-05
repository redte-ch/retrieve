#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import ForeignKey, Index, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._items import Items


class ItemNotes(Items):
    __tablename__ = "itemNotes"
    __table_args__ = (Index("itemNotes_parentItemID", "parentItemID"),)

    itemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    parentItemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE")
    )
    note: Mapped[str | None] = mapped_column(Text)
    title: Mapped[str | None] = mapped_column(Text)

    items: Mapped["Items"] = relationship(
        "Items", foreign_keys=[parentItemID], back_populates="itemNotes"
    )
