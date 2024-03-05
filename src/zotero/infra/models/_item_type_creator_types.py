#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


import datetime
import decimal

from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    Table,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)
from sqlalchemy.sql.sqltypes import NullType

from ._base import Base


class ItemTypeCreatorTypes(Base):
    __tablename__ = "itemTypeCreatorTypes"
    __table_args__ = (Index("itemTypeCreatorTypes_creatorTypeID", "creatorTypeID"),)

    itemTypeID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("itemTypes.itemTypeID"), primary_key=True
    )
    creatorTypeID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("creatorTypes.creatorTypeID"), primary_key=True
    )
    primaryField: Mapped[Optional[int]] = mapped_column(Integer)

    creatorTypes: Mapped["CreatorTypes"] = relationship(
        "CreatorTypes", back_populates="itemTypeCreatorTypes"
    )
    itemTypes: Mapped["ItemTypes"] = relationship(
        "ItemTypes", back_populates="itemTypeCreatorTypes"
    )
