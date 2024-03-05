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


class FieldsCombined(Base):
    __tablename__ = "fieldsCombined"

    fieldID: Mapped[int] = mapped_column(Integer, primary_key=True)
    fieldName: Mapped[str] = mapped_column(Text)
    custom: Mapped[int] = mapped_column(Integer)
    label: Mapped[Optional[str]] = mapped_column(Text)
    fieldFormatID: Mapped[Optional[int]] = mapped_column(Integer)

    itemData: Mapped[List["ItemData"]] = relationship(
        "ItemData", back_populates="fieldsCombined"
    )
