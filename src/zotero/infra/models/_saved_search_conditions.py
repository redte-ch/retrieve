#  Copyleft (ɔ) 2024 Red Innovation.
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


class SavedSearchConditions(Base):
    __tablename__ = "savedSearchConditions"

    savedSearchID: Mapped[int] = mapped_column(
        ForeignKey("savedSearches.savedSearchID", ondelete="CASCADE"), primary_key=True
    )
    searchConditionID: Mapped[int] = mapped_column(Integer, primary_key=True)
    condition: Mapped[str] = mapped_column(Text)
    operator: Mapped[Optional[str]] = mapped_column(Text)
    value: Mapped[Optional[str]] = mapped_column(Text)
    required: Mapped[Optional[decimal.Decimal]] = mapped_column(Numeric)

    savedSearches: Mapped["SavedSearches"] = relationship(
        "SavedSearches", back_populates="savedSearchConditions"
    )
