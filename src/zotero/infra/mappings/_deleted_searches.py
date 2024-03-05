#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Any

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import NullType

from ._saved_searches import SavedSearches


class DeletedSearches(SavedSearches):
    __tablename__ = "deletedSearches"

    dateDeleted: Mapped[Any] = mapped_column(
        NullType, server_default=text("CURRENT_TIMESTAMP")
    )
    savedSearchID: Mapped[int | None] = mapped_column(
        ForeignKey("savedSearches.savedSearchID", ondelete="CASCADE"), primary_key=True
    )
