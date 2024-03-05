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

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class CreatorTypes(Base):
    __tablename__ = "creatorTypes"

    creatorTypeID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    creatorType: Mapped[str | None] = mapped_column(Text)

    itemTypeCreatorTypes: Mapped[list["ItemTypeCreatorTypes"]] = relationship(
        "ItemTypeCreatorTypes", back_populates="creatorTypes"
    )
    itemCreators: Mapped[list["ItemCreators"]] = relationship(
        "ItemCreators", back_populates="creatorTypes"
    )
