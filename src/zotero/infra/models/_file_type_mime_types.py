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

import datetime
import decimal

from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    Table,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)
from sqlalchemy.sql.sqltypes import NullType

from ._base import Base


class FileTypeMimeTypes(Base):
    __tablename__ = "fileTypeMimeTypes"
    __table_args__ = (Index("fileTypeMimeTypes_mimeType", "mimeType"),)

    fileTypeID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("fileTypes.fileTypeID"), primary_key=True
    )
    mimeType: Mapped[Optional[str]] = mapped_column(Text, primary_key=True)

    fileTypes: Mapped["FileTypes"] = relationship(
        "FileTypes", back_populates="fileTypeMimeTypes"
    )
