#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class Users(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(Text)
    userID: Mapped[int | None] = mapped_column(Integer, primary_key=True)

    groupItems: Mapped[list["GroupItems"]] = relationship(
        "GroupItems",
        foreign_keys="[GroupItems.createdByUserID]",
        back_populates="users",
    )
    groupItems_: Mapped[list["GroupItems"]] = relationship(
        "GroupItems",
        foreign_keys="[GroupItems.lastModifiedByUserID]",
        back_populates="users_",
    )
