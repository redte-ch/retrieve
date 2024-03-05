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

from sqlalchemy import Integer, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class Creators(Base):
    __tablename__ = "creators"
    __table_args__ = (UniqueConstraint("lastName", "firstName", "fieldMode"),)

    creatorID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    firstName: Mapped[str | None] = mapped_column(Text)
    lastName: Mapped[str | None] = mapped_column(Text)
    fieldMode: Mapped[int | None] = mapped_column(Integer)

    itemCreators: Mapped[list["ItemCreators"]] = relationship(
        "ItemCreators", back_populates="creators"
    )
