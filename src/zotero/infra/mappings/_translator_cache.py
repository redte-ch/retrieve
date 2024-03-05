#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class TranslatorCache(Base):
    __tablename__ = "translatorCache"

    fileName: Mapped[str | None] = mapped_column(Text, primary_key=True)
    metadataJSON: Mapped[str | None] = mapped_column(Text)
    lastModifiedTime: Mapped[int | None] = mapped_column(Integer)
