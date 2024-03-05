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


class CollectionRelations(Base):
    __tablename__ = "collectionRelations"
    __table_args__ = (
        Index("collectionRelations_object", "object"),
        Index("collectionRelations_predicateID", "predicateID"),
    )

    collectionID: Mapped[int] = mapped_column(
        ForeignKey("collections.collectionID", ondelete="CASCADE"), primary_key=True
    )
    predicateID: Mapped[int] = mapped_column(
        ForeignKey("relationPredicates.predicateID", ondelete="CASCADE"),
        primary_key=True,
    )
    object: Mapped[str] = mapped_column(Text, primary_key=True)

    collections: Mapped["Collections"] = relationship(
        "Collections", back_populates="collectionRelations"
    )
    relationPredicates: Mapped["RelationPredicates"] = relationship(
        "RelationPredicates", back_populates="collectionRelations"
    )
