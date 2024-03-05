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


class Fields(Base):
    __tablename__ = "fields"

    fieldID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    fieldName: Mapped[Optional[str]] = mapped_column(Text)
    fieldFormatID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("fieldFormats.fieldFormatID")
    )

    fieldFormats: Mapped["FieldFormats"] = relationship(
        "FieldFormats", back_populates="fields"
    )
    baseFieldMappings: Mapped[List["BaseFieldMappings"]] = relationship(
        "BaseFieldMappings",
        foreign_keys="[BaseFieldMappings.baseFieldID]",
        back_populates="fields",
    )
    baseFieldMappings_: Mapped[List["BaseFieldMappings"]] = relationship(
        "BaseFieldMappings",
        foreign_keys="[BaseFieldMappings.fieldID]",
        back_populates="fields_",
    )
    customBaseFieldMappings: Mapped[List["CustomBaseFieldMappings"]] = relationship(
        "CustomBaseFieldMappings", back_populates="fields"
    )
    customItemTypeFields: Mapped[List["CustomItemTypeFields"]] = relationship(
        "CustomItemTypeFields", back_populates="fields"
    )
    itemTypeFields: Mapped[List["ItemTypeFields"]] = relationship(
        "ItemTypeFields", back_populates="fields"
    )
