#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Any

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import NullType

from ._base import Base


class ItemDataValues(Base):
    __tablename__ = "itemDataValues"

    valueID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    value: Mapped[Any | None] = mapped_column(NullType)

    itemData: Mapped[list["ItemData"]] = relationship(
        "ItemData", back_populates="itemDataValues"
    )
