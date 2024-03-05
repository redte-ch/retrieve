#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class FulltextWords(Base):
    __tablename__ = "fulltextWords"

    wordID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    word: Mapped[str | None] = mapped_column(Text, unique=True)

    items: Mapped[list["Items"]] = relationship(
        "Items", secondary="fulltextItemWords", back_populates="fulltextWords"
    )
