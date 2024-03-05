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


class Users(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(Text)
    userID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)

    groupItems: Mapped[List["GroupItems"]] = relationship(
        "GroupItems",
        foreign_keys="[GroupItems.createdByUserID]",
        back_populates="users",
    )
    groupItems_: Mapped[List["GroupItems"]] = relationship(
        "GroupItems",
        foreign_keys="[GroupItems.lastModifiedByUserID]",
        back_populates="users_",
    )
