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

from sqlalchemy import TIMESTAMP, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from ._items import Items


class FeedItems(Items):
    __tablename__ = "feedItems"

    guid: Mapped[str] = mapped_column(Text, unique=True)
    itemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    readTime: Mapped[datetime.datetime | None] = mapped_column(TIMESTAMP)
    translatedTime: Mapped[datetime.datetime | None] = mapped_column(TIMESTAMP)
