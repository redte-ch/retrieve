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


class CustomItemTypeFields(Base):
    __tablename__ = "customItemTypeFields"
    __table_args__ = (
        Index("customItemTypeFields_customFieldID", "customFieldID"),
        Index("customItemTypeFields_fieldID", "fieldID"),
    )

    customItemTypeID: Mapped[int] = mapped_column(
        ForeignKey("customItemTypes.customItemTypeID"), primary_key=True
    )
    hide: Mapped[int] = mapped_column(Integer)
    orderIndex: Mapped[int] = mapped_column(Integer, primary_key=True)
    fieldID: Mapped[Optional[int]] = mapped_column(ForeignKey("fields.fieldID"))
    customFieldID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("customFields.customFieldID")
    )

    customFields: Mapped["CustomFields"] = relationship(
        "CustomFields", back_populates="customItemTypeFields"
    )
    customItemTypes: Mapped["CustomItemTypes"] = relationship(
        "CustomItemTypes", back_populates="customItemTypeFields"
    )
    fields: Mapped["Fields"] = relationship(
        "Fields", back_populates="customItemTypeFields"
    )
