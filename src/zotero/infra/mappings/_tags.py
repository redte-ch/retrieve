#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class Tags(Base):
    __tablename__ = "tags"

    name: Mapped[str] = mapped_column(Text, unique=True)
    tagID: Mapped[int | None] = mapped_column(Integer, primary_key=True)

    itemTags: Mapped[list["ItemTags"]] = relationship("ItemTags", back_populates="tags")
