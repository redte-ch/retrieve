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

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class FieldsCombined(Base):
    __tablename__ = "fieldsCombined"

    fieldID: Mapped[int] = mapped_column(Integer, primary_key=True)
    fieldName: Mapped[str] = mapped_column(Text)
    custom: Mapped[int] = mapped_column(Integer)
    label: Mapped[str | None] = mapped_column(Text)
    fieldFormatID: Mapped[int | None] = mapped_column(Integer)

    itemData: Mapped[list["ItemData"]] = relationship(
        "ItemData", back_populates="fieldsCombined"
    )
