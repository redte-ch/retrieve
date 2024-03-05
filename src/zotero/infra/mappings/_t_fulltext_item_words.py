#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12


from sqlalchemy import Column, ForeignKey, Index, Table

from ._base import Base

t_fulltextItemWords = Table(
    "fulltextItemWords",
    Base.metadata,
    Column("wordID", ForeignKey("fulltextWords.wordID"), primary_key=True),
    Column("itemID", ForeignKey("items.itemID", ondelete="CASCADE"), primary_key=True),
    Index("fulltextItemWords_itemID", "itemID"),
)
