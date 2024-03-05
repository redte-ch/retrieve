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

from sqlalchemy import ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ._base import Base


class CustomBaseFieldMappings(Base):
    __tablename__ = "customBaseFieldMappings"
    __table_args__ = (
        Index("customBaseFieldMappings_baseFieldID", "baseFieldID"),
        Index("customBaseFieldMappings_customFieldID", "customFieldID"),
    )

    customItemTypeID: Mapped[int | None] = mapped_column(
        ForeignKey("customItemTypes.customItemTypeID"), primary_key=True
    )
    baseFieldID: Mapped[int | None] = mapped_column(
        ForeignKey("fields.fieldID"), primary_key=True
    )
    customFieldID: Mapped[int | None] = mapped_column(
        ForeignKey("customFields.customFieldID"), primary_key=True
    )

    fields: Mapped["Fields"] = relationship(
        "Fields", back_populates="customBaseFieldMappings"
    )
    customFields: Mapped["CustomFields"] = relationship(
        "CustomFields", back_populates="customBaseFieldMappings"
    )
    customItemTypes: Mapped["CustomItemTypes"] = relationship(
        "CustomItemTypes", back_populates="customBaseFieldMappings"
    )
