#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class PublicationsItems(Base):
    __tablename__ = "publicationsItems"

    itemID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
