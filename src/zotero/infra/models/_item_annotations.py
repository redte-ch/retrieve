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


class ItemAnnotations(Items):
    __tablename__ = "itemAnnotations"
    __table_args__ = (Index("itemAnnotations_parentItemID", "parentItemID"),)

    parentItemID: Mapped[int] = mapped_column(ForeignKey("itemAttachments.itemID"))
    type: Mapped[int] = mapped_column(Integer)
    sortIndex: Mapped[str] = mapped_column(Text)
    position: Mapped[str] = mapped_column(Text)
    isExternal: Mapped[int] = mapped_column(Integer)
    itemID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    authorName: Mapped[Optional[str]] = mapped_column(Text)
    text_: Mapped[Optional[str]] = mapped_column("text", Text)
    comment: Mapped[Optional[str]] = mapped_column(Text)
    color: Mapped[Optional[str]] = mapped_column(Text)
    pageLabel: Mapped[Optional[str]] = mapped_column(Text)

    itemAttachments: Mapped["ItemAttachments"] = relationship(
        "ItemAttachments", back_populates="itemAnnotations"
    )
