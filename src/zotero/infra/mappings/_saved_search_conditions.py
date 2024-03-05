#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import decimal

from sqlalchemy import ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import NullType

from ._base import Base


class SavedSearchConditions(Base):
    __tablename__ = "savedSearchConditions"

    savedSearchID: Mapped[int] = mapped_column(
        ForeignKey("savedSearches.savedSearchID", ondelete="CASCADE"), primary_key=True
    )
    searchConditionID: Mapped[int] = mapped_column(Integer, primary_key=True)
    condition: Mapped[str] = mapped_column(Text)
    operator: Mapped[str | None] = mapped_column(Text)
    value: Mapped[str | None] = mapped_column(Text)
    required: Mapped[decimal.Decimal | None] = mapped_column(Numeric)

    savedSearches: Mapped["SavedSearches"] = relationship(
        "SavedSearches", back_populates="savedSearchConditions"
    )
