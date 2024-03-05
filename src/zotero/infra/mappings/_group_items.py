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

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._items import Items


class GroupItems(Items):
    __tablename__ = "groupItems"

    itemID: Mapped[int | None] = mapped_column(
        ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True
    )
    createdByUserID: Mapped[int | None] = mapped_column(
        ForeignKey("users.userID", ondelete="SET NULL")
    )
    lastModifiedByUserID: Mapped[int | None] = mapped_column(
        ForeignKey("users.userID", ondelete="SET NULL")
    )

    users: Mapped["Users"] = relationship(
        "Users", foreign_keys=[createdByUserID], back_populates="groupItems"
    )
    users_: Mapped["Users"] = relationship(
        "Users", foreign_keys=[lastModifiedByUserID], back_populates="groupItems_"
    )
