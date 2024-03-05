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


class FulltextItems(Items):
    __tablename__ = "fulltextItems"
    __table_args__ = (
        Index("fulltextItems_synced", "synced"),
        Index("fulltextItems_version", "version"),
    )

    version: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    synced: Mapped[int] = mapped_column(Integer, server_default=text("0"))
    itemID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    indexedPages: Mapped[Optional[int]] = mapped_column(Integer)
    totalPages: Mapped[Optional[int]] = mapped_column(Integer)
    indexedChars: Mapped[Optional[int]] = mapped_column(Integer)
    totalChars: Mapped[Optional[int]] = mapped_column(Integer)
