#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import Index, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class ItemTypeFieldsCombined(Base):
    __tablename__ = "itemTypeFieldsCombined"
    __table_args__ = (
        UniqueConstraint("itemTypeID", "fieldID"),
        Index("itemTypeFieldsCombined_fieldID", "fieldID"),
    )

    itemTypeID: Mapped[int] = mapped_column(Integer, primary_key=True)
    fieldID: Mapped[int] = mapped_column(Integer)
    orderIndex: Mapped[int] = mapped_column(Integer, primary_key=True)
    hide: Mapped[int | None] = mapped_column(Integer)
