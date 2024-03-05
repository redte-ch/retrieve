#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Any

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import NullType

from ._base import Base


class Settings(Base):
    __tablename__ = "settings"

    setting: Mapped[str | None] = mapped_column(Text, primary_key=True)
    key: Mapped[str | None] = mapped_column(Text, primary_key=True)
    value: Mapped[Any | None] = mapped_column(NullType)
