#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class RelationPredicates(Base):
    __tablename__ = "relationPredicates"

    predicateID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    predicate: Mapped[str | None] = mapped_column(Text, unique=True)

    collectionRelations: Mapped[list["CollectionRelations"]] = relationship(
        "CollectionRelations", back_populates="relationPredicates"
    )
    itemRelations: Mapped[list["ItemRelations"]] = relationship(
        "ItemRelations", back_populates="relationPredicates"
    )
