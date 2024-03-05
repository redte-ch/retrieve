#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import Integer, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class Libraries(Base):
    __tablename__ = "libraries"

    type: Mapped[str] = mapped_column(Text)
    editable: Mapped[int] = mapped_column(Integer)
    filesEditable: Mapped[int] = mapped_column(Integer)
    version: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    storageVersion: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    lastSync: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    archived: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    libraryID: Mapped[int | None] = mapped_column(Integer, primary_key=True)

    collections: Mapped[list["Collections"]] = relationship(
        "Collections", back_populates="libraries"
    )
    groups: Mapped["Groups"] = relationship(
        "Groups", uselist=False, back_populates="libraries"
    )
    items: Mapped[list["Items"]] = relationship("Items", back_populates="libraries")
    savedSearches: Mapped[list["SavedSearches"]] = relationship(
        "SavedSearches", back_populates="libraries"
    )
    storageDeleteLog: Mapped[list["StorageDeleteLog"]] = relationship(
        "StorageDeleteLog", back_populates="libraries"
    )
    syncCache: Mapped[list["SyncCache"]] = relationship(
        "SyncCache", back_populates="libraries"
    )
    syncQueue: Mapped[list["SyncQueue"]] = relationship(
        "SyncQueue", back_populates="libraries"
    )
    syncedSettings: Mapped[list["SyncedSettings"]] = relationship(
        "SyncedSettings", back_populates="libraries"
    )
