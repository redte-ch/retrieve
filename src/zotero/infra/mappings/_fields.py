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

from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class Fields(Base):
    __tablename__ = "fields"

    fieldID: Mapped[int | None] = mapped_column(Integer, primary_key=True)
    fieldName: Mapped[str | None] = mapped_column(Text)
    fieldFormatID: Mapped[int | None] = mapped_column(
        ForeignKey("fieldFormats.fieldFormatID")
    )

    fieldFormats: Mapped["FieldFormats"] = relationship(
        "FieldFormats", back_populates="fields"
    )
    baseFieldMappings: Mapped[list["BaseFieldMappings"]] = relationship(
        "BaseFieldMappings",
        foreign_keys="[BaseFieldMappings.baseFieldID]",
        back_populates="fields",
    )
    baseFieldMappings_: Mapped[list["BaseFieldMappings"]] = relationship(
        "BaseFieldMappings",
        foreign_keys="[BaseFieldMappings.fieldID]",
        back_populates="fields_",
    )
    customBaseFieldMappings: Mapped[list["CustomBaseFieldMappings"]] = relationship(
        "CustomBaseFieldMappings", back_populates="fields"
    )
    customItemTypeFields: Mapped[list["CustomItemTypeFields"]] = relationship(
        "CustomItemTypeFields", back_populates="fields"
    )
    itemTypeFields: Mapped[list["ItemTypeFields"]] = relationship(
        "ItemTypeFields", back_populates="fields"
    )
