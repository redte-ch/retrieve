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


class CustomBaseFieldMappings(Base):
    __tablename__ = "customBaseFieldMappings"
    __table_args__ = (
        Index("customBaseFieldMappings_baseFieldID", "baseFieldID"),
        Index("customBaseFieldMappings_customFieldID", "customFieldID"),
    )

    customItemTypeID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("customItemTypes.customItemTypeID"), primary_key=True
    )
    baseFieldID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("fields.fieldID"), primary_key=True
    )
    customFieldID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("customFields.customFieldID"), primary_key=True
    )

    fields: Mapped["Fields"] = relationship(
        "Fields", back_populates="customBaseFieldMappings"
    )
    customFields: Mapped["CustomFields"] = relationship(
        "CustomFields", back_populates="customBaseFieldMappings"
    )
    customItemTypes: Mapped["CustomItemTypes"] = relationship(
        "CustomItemTypes", back_populates="customBaseFieldMappings"
    )
