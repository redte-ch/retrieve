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

from typing import Any

from sqlalchemy import ForeignKey, Index, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import NullType

from ._items import Items


class DeletedItems(Items):
    __tablename__ = "deletedItems"
    __table_args__ = (
        Index("deletedItems_dateDeleted", "dateDeleted"),
        Index("deletedSearches_dateDeleted", "dateDeleted"),
    )

    dateDeleted: Mapped[Any] = mapped_column(
        NullType, server_default=text("CURRENT_TIMESTAMP")
    )
    itemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
