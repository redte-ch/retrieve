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


class ItemNotes(Items):
    __tablename__ = "itemNotes"
    __table_args__ = (Index("itemNotes_parentItemID", "parentItemID"),)

    itemID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    parentItemID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE")
    )
    note: Mapped[Optional[str]] = mapped_column(Text)
    title: Mapped[Optional[str]] = mapped_column(Text)

    items: Mapped["Items"] = relationship(
        "Items", foreign_keys=[parentItemID], back_populates="itemNotes"
    )
