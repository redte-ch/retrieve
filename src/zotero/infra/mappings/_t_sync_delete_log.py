#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Column, ForeignKey, Table, Text, UniqueConstraint, text

from ._base import Base

t_syncDeleteLog = Table(
    "syncDeleteLog",
    Base.metadata,
    Column(
        "syncObjectTypeID",
        ForeignKey("syncObjectTypes.syncObjectTypeID"),
        nullable=False,
    ),
    Column(
        "libraryID",
        ForeignKey("libraries.libraryID", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("key", Text, nullable=False),
    Column(
        "dateDeleted", Text, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    ),
    UniqueConstraint("syncObjectTypeID", "libraryID", "key"),
)
