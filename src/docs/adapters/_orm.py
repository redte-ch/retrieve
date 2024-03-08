#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

from sqlmodel import Field, SQLModel, Relationship


class Library(SQLModel, table=True):
    libraryID: int = Field(primary_key=True)
    type: str
    editable: int
    filesEditable: int


class Collection(SQLModel, table=True):
    collectionID: int = Field(primary_key=True)
    collectionName: str = Field(default=None, nullable=False)
    parentCollectionID: int = Field(default=None, foreign_key="collections.collectionID")
    libraryID: int = Field(default=None, foreign_key="libraries.libraryID", nullable=False)
    key: str = Field(default=None, nullable=False)

    # Relationships
    parent_collection: Collection | None = Relationship(back_populates="collections")
    library: Library | None = Relationship(back_populates="collections")


class Item(SQLModel, table=True):
    itemID: int = Field(primary_key=True)
    itemTypeID: int = Field(default=None, nullable=False)
    libraryID: int = Field(default=None, foreign_key="libraries.libraryID", nullable=False)
    key: str = Field(default=None, nullable=False)

    # Relationships
    library: Library | None = Relationship(back_populates="items")


class ItemAttachment(SQLModel, table=True):
    itemID: int = Field(primary_key=True, foreign_key="items.itemID")
    parentItemID: int | None = Field(default=None, foreign_key="items.itemID")
    linkMode: int
    contentType: str | None
    charsetID: int | None = Field(default=None, foreign_key="charsets.charsetID")
    path: str | None
    storageHash: str | None

    # Relationships
    item: Item | None = Relationship(back_populates="itemAttachments")
    parent_item: Item | None = Relationship(back_populates="itemAttachments")
