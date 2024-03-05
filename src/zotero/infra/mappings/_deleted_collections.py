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

from ._collections import Collections


class DeletedCollections(Collections):
    __tablename__ = "deletedCollections"
    __table_args__ = (Index("deletedCollections_dateDeleted", "dateDeleted"),)

    dateDeleted: Mapped[Any] = mapped_column(
        NullType, server_default=text("CURRENT_TIMESTAMP")
    )
    collectionID: Mapped[int | None] = mapped_column(
        ForeignKey("collections.collectionID", ondelete="CASCADE"), primary_key=True
    )
