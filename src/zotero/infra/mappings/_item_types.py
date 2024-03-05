#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import Integer, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class ItemTypes(Base):
    __tablename__ = "itemTypes"

    itemTypeID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    typeName: Mapped[str | None] = mapped_column(Text)
    templateItemTypeID: Mapped[int | None] = mapped_column(Integer)
    display: Mapped[int | None] = mapped_column(Integer, server_default=text("1"))

    itemTypeCreatorTypes: Mapped[list["ItemTypeCreatorTypes"]] = relationship(
        "ItemTypeCreatorTypes", back_populates="itemTypes"
    )
    baseFieldMappings: Mapped[list["BaseFieldMappings"]] = relationship(
        "BaseFieldMappings", back_populates="itemTypes"
    )
    itemTypeFields: Mapped[list["ItemTypeFields"]] = relationship(
        "ItemTypeFields", back_populates="itemTypes"
    )
