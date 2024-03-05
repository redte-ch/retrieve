#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import Integer, Text, text
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class ItemTypesCombined(Base):
    __tablename__ = "itemTypesCombined"

    itemTypeID: Mapped[int] = mapped_column(Integer, primary_key=True)
    typeName: Mapped[str] = mapped_column(Text)
    display: Mapped[int] = mapped_column(Integer, server_default=text("1"))
    custom: Mapped[int] = mapped_column(Integer)
