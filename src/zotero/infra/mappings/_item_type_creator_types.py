#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import ForeignKey, Index, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class ItemTypeCreatorTypes(Base):
    __tablename__ = "itemTypeCreatorTypes"
    __table_args__ = (Index("itemTypeCreatorTypes_creatorTypeID", "creatorTypeID"),)

    itemTypeID: Mapped[int | None] = mapped_column(
        ForeignKey("itemTypes.itemTypeID"), primary_key=True
    )
    creatorTypeID: Mapped[int | None] = mapped_column(
        ForeignKey("creatorTypes.creatorTypeID"), primary_key=True
    )
    primaryField: Mapped[int | None] = mapped_column(Integer)

    creatorTypes: Mapped["CreatorTypes"] = relationship(
        "CreatorTypes", back_populates="itemTypeCreatorTypes"
    )
    itemTypes: Mapped["ItemTypes"] = relationship(
        "ItemTypes", back_populates="itemTypeCreatorTypes"
    )
