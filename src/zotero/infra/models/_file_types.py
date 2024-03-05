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


class FileTypes(Base):
    __tablename__ = "fileTypes"
    __table_args__ = (Index("fileTypes_fileType", "fileType"),)

    fileTypeID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)
    fileType: Mapped[Optional[str]] = mapped_column(Text, unique=True)

    fileTypeMimeTypes: Mapped[List["FileTypeMimeTypes"]] = relationship(
        "FileTypeMimeTypes", back_populates="fileTypes"
    )
