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


class BaseFieldMappings(Base):
    __tablename__ = "baseFieldMappings"
    __table_args__ = (
        Index("baseFieldMappings_baseFieldID", "baseFieldID"),
        Index("baseFieldMappings_fieldID", "fieldID"),
    )

    itemTypeID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("itemTypes.itemTypeID"), primary_key=True
    )
    baseFieldID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("fields.fieldID"), primary_key=True
    )
    fieldID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("fields.fieldID"), primary_key=True
    )

    fields: Mapped["Fields"] = relationship(
        "Fields", foreign_keys=[baseFieldID], back_populates="baseFieldMappings"
    )
    fields_: Mapped["Fields"] = relationship(
        "Fields", foreign_keys=[fieldID], back_populates="baseFieldMappings_"
    )
    itemTypes: Mapped["ItemTypes"] = relationship(
        "ItemTypes", back_populates="baseFieldMappings"
    )
