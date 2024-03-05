#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import datetime

from sqlalchemy import TIMESTAMP, ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from ._libraries import Libraries


class Feeds(Libraries):
    __tablename__ = "feeds"

    name: Mapped[str] = mapped_column(Text)
    url: Mapped[str] = mapped_column(Text, unique=True)
    libraryID: Mapped[int | None] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE"), primary_key=True
    )
    lastUpdate: Mapped[datetime.datetime | None] = mapped_column(TIMESTAMP)
    lastCheck: Mapped[datetime.datetime | None] = mapped_column(TIMESTAMP)
    lastCheckError: Mapped[str | None] = mapped_column(Text)
    cleanupReadAfter: Mapped[int | None] = mapped_column(Integer)
    cleanupUnreadAfter: Mapped[int | None] = mapped_column(Integer)
    refreshInterval: Mapped[int | None] = mapped_column(Integer)
