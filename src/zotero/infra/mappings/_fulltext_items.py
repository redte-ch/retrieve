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

from sqlalchemy import ForeignKey, Index, Integer, text
from sqlalchemy.orm import Mapped, mapped_column

from ._items import Items


class FulltextItems(Items):
    __tablename__ = "fulltextItems"
    __table_args__ = (
        Index("fulltextItems_synced", "synced"),
        Index("fulltextItems_version", "version"),
    )

    version: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    synced: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    itemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    indexedPages: Mapped[int | None] = mapped_column(Integer)
    totalPages: Mapped[int | None] = mapped_column(Integer)
    indexedChars: Mapped[int | None] = mapped_column(Integer)
    totalChars: Mapped[int | None] = mapped_column(Integer)
