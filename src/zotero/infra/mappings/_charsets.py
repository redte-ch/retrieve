#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Index, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class Charsets(Base):
    __tablename__ = "charsets"
    __table_args__ = (Index("charsets_charset", "charset"),)

    charsetID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    charset: Mapped[str | None] = mapped_column(Text, unique=True)

    itemAttachments: Mapped[list["ItemAttachments"]] = relationship(
        "ItemAttachments", back_populates="charsets"
    )
