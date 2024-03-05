#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import ForeignKey, Integer, Text, text
from sqlalchemy.orm import Mapped, mapped_column

from ._items import Items


class RetractedItems(Items):
    __tablename__ = "retractedItems"

    itemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    data: Mapped[str | None] = mapped_column(Text)
    flag: Mapped[int | None] = mapped_column(Integer, server_default=text("0"))
