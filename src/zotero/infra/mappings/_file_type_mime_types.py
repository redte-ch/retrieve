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

from sqlalchemy import ForeignKey, Index, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class FileTypeMimeTypes(Base):
    __tablename__ = "fileTypeMimeTypes"
    __table_args__ = (Index("fileTypeMimeTypes_mimeType", "mimeType"),)

    fileTypeID: Mapped[int | None] = mapped_column(
        ForeignKey("fileTypes.fileTypeID"), primary_key=True
    )
    mimeType: Mapped[str | None] = mapped_column(Text, primary_key=True)

    fileTypes: Mapped["FileTypes"] = relationship(
        "FileTypes", back_populates="fileTypeMimeTypes"
    )
