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

from sqlalchemy import Integer, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class CustomItemTypes(Base):
    __tablename__ = "customItemTypes"

    customItemTypeID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    typeName: Mapped[str | None] = mapped_column(Text)
    label: Mapped[str | None] = mapped_column(Text)
    display: Mapped[int | None] = mapped_column(Integer, server_default=text("1"))
    icon: Mapped[str | None] = mapped_column(Text)

    customBaseFieldMappings: Mapped[list["CustomBaseFieldMappings"]] = relationship(
        "CustomBaseFieldMappings", back_populates="customItemTypes"
    )
    customItemTypeFields: Mapped[list["CustomItemTypeFields"]] = relationship(
        "CustomItemTypeFields", back_populates="customItemTypes"
    )
