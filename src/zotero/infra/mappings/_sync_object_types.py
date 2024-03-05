#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Index, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class SyncObjectTypes(Base):
    __tablename__ = "syncObjectTypes"
    __table_args__ = (Index("syncObjectTypes_name", "name"),)

    syncObjectTypeID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    name: Mapped[str | None] = mapped_column(Text)

    syncCache: Mapped[list["SyncCache"]] = relationship(
        "SyncCache", back_populates="syncObjectTypes"
    )
    syncQueue: Mapped[list["SyncQueue"]] = relationship(
        "SyncQueue", back_populates="syncObjectTypes"
    )
