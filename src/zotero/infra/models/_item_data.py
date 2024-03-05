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


class ItemData(Base):
    __tablename__ = "itemData"
    __table_args__ = (Index("itemData_fieldID", "fieldID"),)

    itemID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    fieldID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("fieldsCombined.fieldID"), primary_key=True
    )
    valueID: Mapped[Optional[int]] = mapped_column(ForeignKey("itemDataValues.valueID"))

    fieldsCombined: Mapped["FieldsCombined"] = relationship(
        "FieldsCombined", back_populates="itemData"
    )
    items: Mapped["Items"] = relationship("Items", back_populates="itemData")
    itemDataValues: Mapped["ItemDataValues"] = relationship(
        "ItemDataValues", back_populates="itemData"
    )
