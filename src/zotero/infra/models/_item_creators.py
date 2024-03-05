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


class ItemCreators(Base):
    __tablename__ = "itemCreators"
    __table_args__ = (
        UniqueConstraint("itemID", "orderIndex"),
        Index("itemCreators_creatorTypeID", "creatorTypeID"),
    )

    itemID: Mapped[int] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    creatorID: Mapped[int] = mapped_column(
        ForeignKey("creators.creatorID", ondelete="CASCADE"), primary_key=True
    )
    creatorTypeID: Mapped[int] = mapped_column(
        ForeignKey("creatorTypes.creatorTypeID"),
        primary_key=True,
        server_default=text("1"),
    )
    orderIndex: Mapped[int] = mapped_column(
        Integer, primary_key=True, server_default=text("0")
    )

    creators: Mapped["Creators"] = relationship(
        "Creators", back_populates="itemCreators"
    )
    creatorTypes: Mapped["CreatorTypes"] = relationship(
        "CreatorTypes", back_populates="itemCreators"
    )
    items: Mapped["Items"] = relationship("Items", back_populates="itemCreators")
