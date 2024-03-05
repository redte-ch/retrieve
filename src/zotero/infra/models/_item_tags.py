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


class ItemTags(Base):
    __tablename__ = "itemTags"
    __table_args__ = (Index("itemTags_tagID", "tagID"),)

    itemID: Mapped[int] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    tagID: Mapped[int] = mapped_column(
        ForeignKey("tags.tagID", ondelete="CASCADE"), primary_key=True
    )
    type: Mapped[int] = mapped_column(Integer)

    items: Mapped["Items"] = relationship("Items", back_populates="itemTags")
    tags: Mapped["Tags"] = relationship("Tags", back_populates="itemTags")
