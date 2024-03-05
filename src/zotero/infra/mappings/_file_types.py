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

from sqlalchemy import Index, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class FileTypes(Base):
    __tablename__ = "fileTypes"
    __table_args__ = (Index("fileTypes_fileType", "fileType"),)

    fileTypeID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    fileType: Mapped[str | None] = mapped_column(Text, unique=True)

    fileTypeMimeTypes: Mapped[list["FileTypeMimeTypes"]] = relationship(
        "FileTypeMimeTypes", back_populates="fileTypes"
    )
