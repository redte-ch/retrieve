#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import ForeignKey, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class StorageDeleteLog(Base):
    __tablename__ = "storageDeleteLog"

    libraryID: Mapped[int] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE"), primary_key=True
    )
    key: Mapped[str] = mapped_column(Text, primary_key=True)
    dateDeleted: Mapped[str] = mapped_column(
        Text, server_default=text("CURRENT_TIMESTAMP")
    )

    libraries: Mapped["Libraries"] = relationship(
        "Libraries", back_populates="storageDeleteLog"
    )
