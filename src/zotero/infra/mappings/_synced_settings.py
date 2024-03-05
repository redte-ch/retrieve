#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Any

from sqlalchemy import ForeignKey, Integer, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import NullType

from ._base import Base


class SyncedSettings(Base):
    __tablename__ = "syncedSettings"

    setting: Mapped[str] = mapped_column(Text, primary_key=True)
    libraryID: Mapped[int] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE"), primary_key=True
    )
    value: Mapped[Any] = mapped_column(NullType)
    version: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    synced: Mapped[int] = mapped_column(Integer, server_default=text("0"))

    libraries: Mapped["Libraries"] = relationship(
        "Libraries", back_populates="syncedSettings"
    )
