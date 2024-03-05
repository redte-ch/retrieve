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

from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class FieldFormats(Base):
    __tablename__ = "fieldFormats"

    fieldFormatID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    regex: Mapped[str | None] = mapped_column(Text)
    isInteger: Mapped[int | None] = mapped_column(Integer)

    fields: Mapped[list["Fields"]] = relationship(
        "Fields", back_populates="fieldFormats"
    )
