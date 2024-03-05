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

from sqlalchemy import Index, Integer
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class BaseFieldMappingsCombined(Base):
    __tablename__ = "baseFieldMappingsCombined"
    __table_args__ = (
        Index("baseFieldMappingsCombined_baseFieldID", "baseFieldID"),
        Index("baseFieldMappingsCombined_fieldID", "fieldID"),
    )

    itemTypeID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    baseFieldID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    fieldID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
