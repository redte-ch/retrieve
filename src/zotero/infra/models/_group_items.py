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


class GroupItems(Items):
    __tablename__ = "groupItems"

    itemID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    createdByUserID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.userID", ondelete="SET NULL")
    )
    lastModifiedByUserID: Mapped[Optional[int]] = mapped_column(
        ForeignKey("users.userID", ondelete="SET NULL")
    )

    users: Mapped["Users"] = relationship(
        "Users", foreign_keys=[createdByUserID], back_populates="groupItems"
    )
    users_: Mapped["Users"] = relationship(
        "Users", foreign_keys=[lastModifiedByUserID], back_populates="groupItems_"
    )
