#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import Index, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class Version(Base):
    __tablename__ = "version"
    __table_args__ = (Index("schema", "schema"),)

    version: Mapped[int] = mapped_column(Integer)
    schema: Mapped[str | None] = mapped_column(Text, primary_key=True)
