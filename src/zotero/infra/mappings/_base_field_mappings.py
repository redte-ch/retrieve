#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from sqlalchemy import ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class BaseFieldMappings(Base):
    __tablename__ = "baseFieldMappings"
    __table_args__ = (
        Index("baseFieldMappings_baseFieldID", "baseFieldID"),
        Index("baseFieldMappings_fieldID", "fieldID"),
    )

    itemTypeID: Mapped[int | None] = mapped_column(
        ForeignKey("itemTypes.itemTypeID"), primary_key=True
    )
    baseFieldID: Mapped[int | None] = mapped_column(
        ForeignKey("fields.fieldID"), primary_key=True
    )
    fieldID: Mapped[int | None] = mapped_column(
        ForeignKey("fields.fieldID"), primary_key=True
    )

    fields: Mapped["Fields"] = relationship(
        "Fields", foreign_keys=[baseFieldID], back_populates="baseFieldMappings"
    )
    fields_: Mapped["Fields"] = relationship(
        "Fields", foreign_keys=[fieldID], back_populates="baseFieldMappings_"
    )
    itemTypes: Mapped["ItemTypes"] = relationship(
        "ItemTypes", back_populates="baseFieldMappings"
    )
