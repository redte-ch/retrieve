#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import datetime

from sqlalchemy import (
    TIMESTAMP,
    ForeignKey,
    Index,
    Integer,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class SavedSearches(Base):
    __tablename__ = "savedSearches"
    __table_args__ = (
        UniqueConstraint("libraryID", "key"),
        Index("savedSearches_synced", "synced"),
    )

    savedSearchName: Mapped[str] = mapped_column(Text)
    clientDateModified: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
    )
    libraryID: Mapped[int] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE")
    )
    key: Mapped[str] = mapped_column(Text)
    version: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    synced: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    savedSearchID: Mapped[int | None] = mapped_column(Integer, primary_key=True)

    libraries: Mapped["Libraries"] = relationship(
        "Libraries", back_populates="savedSearches"
    )
    savedSearchConditions: Mapped[list["SavedSearchConditions"]] = relationship(
        "SavedSearchConditions", back_populates="savedSearches"
    )
