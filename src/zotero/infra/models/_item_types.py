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


class ItemTypes(Base):
    __tablename__ = "itemTypes"

    itemTypeID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    typeName: Mapped[Optional[str]] = mapped_column(Text)
    templateItemTypeID: Mapped[Optional[int]] = mapped_column(Integer)
    display: Mapped[Optional[int]] = mapped_column(Integer, server_default=text("1"))

    itemTypeCreatorTypes: Mapped[List["ItemTypeCreatorTypes"]] = relationship(
        "ItemTypeCreatorTypes", back_populates="itemTypes"
    )
    baseFieldMappings: Mapped[List["BaseFieldMappings"]] = relationship(
        "BaseFieldMappings", back_populates="itemTypes"
    )
    itemTypeFields: Mapped[List["ItemTypeFields"]] = relationship(
        "ItemTypeFields", back_populates="itemTypes"
    )
