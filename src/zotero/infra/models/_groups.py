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


class Groups(Base):
    __tablename__ = "groups"

    libraryID: Mapped[int] = mapped_column(
        ForeignKey("libraries.libraryID", ondelete="CASCADE"), unique=True
    )
    name: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    version: Mapped[int] = mapped_column(Integer)
    groupID: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True)

    libraries: Mapped["Libraries"] = relationship("Libraries", back_populates="groups")
