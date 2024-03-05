#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import ForeignKey, Index, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class ItemRelations(Base):
    __tablename__ = "itemRelations"
    __table_args__ = (
        Index("itemRelations_object", "object"),
        Index("itemRelations_predicateID", "predicateID"),
    )

    itemID: Mapped[int] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    predicateID: Mapped[int] = mapped_column(
        ForeignKey("relationPredicates.predicateID", ondelete="CASCADE"),
        primary_key=True,
    )
    object: Mapped[str] = mapped_column(Text, primary_key=True)

    items: Mapped["Items"] = relationship("Items", back_populates="itemRelations")
    relationPredicates: Mapped["RelationPredicates"] = relationship(
        "RelationPredicates", back_populates="itemRelations"
    )
