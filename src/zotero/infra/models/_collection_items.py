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


class CollectionItems(Base):
    __tablename__ = "collectionItems"
    __table_args__ = (Index("collectionItems_itemID", "itemID"),)

    collectionID: Mapped[int] = mapped_column(
        ForeignKey("collections.collectionID", ondelete="CASCADE"), primary_key=True
    )
    itemID: Mapped[int] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    orderIndex: Mapped[int] = mapped_column(Integer, server_default=text("0"))

    collections: Mapped["Collections"] = relationship(
        "Collections", back_populates="collectionItems"
    )
    items: Mapped["Items"] = relationship("Items", back_populates="collectionItems")
