#  Copyleft (ɔ) 2024 Red Innovation.

#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from docs.domain import Library, Collection, Item, File


class Libraries(SQLModel, table=True):
    libraryID: int = Field(primary_key=True)
    type: str
    editable: int
    filesEditable: int
    collections: Optional[list["Collections"]] = Relationship(back_populates="library")
    items: Optional[list["Items"]] = Relationship(back_populates="library")

    @classmethod
    def from_model(cls, model: Library) -> "Libraries":
        return cls(
            libraryID=model.id,
            type=model.type,
            editable=model.editable,
            filesEditable=model.filesEditable,
        )

    def to_model(self) -> Library:
        return Library(
            id=self.libraryID,
            type=self.type,
            editable=self.editable,
            filesEditable=self.filesEditable,
        )


class Collections(SQLModel, table=True):
    collectionID: int = Field(primary_key=True)
    collectionName: str = Field(default=None, nullable=False)
    parentCollectionID: int = Field(
        default=None, foreign_key="collections.collectionID"
    )
    libraryID: int = Field(
        default=None, foreign_key="libraries.libraryID", nullable=False
    )
    key: str = Field(default=None, nullable=False)
    library: Optional[Libraries] = Relationship(back_populates="collections")

    @classmethod
    def from_model(cls, model: Collection) -> "Collections":
        return cls(
            collectionID=model.id,
        )

    def to_model(self) -> Collection:
        return Collection(
            id=self.collectionID,
        )


class Items(SQLModel, table=True):
    itemID: int = Field(primary_key=True)
    itemTypeID: int = Field(default=None, nullable=False)
    libraryID: int = Field(
        default=None, foreign_key="libraries.libraryID", nullable=False
    )
    key: str = Field(default=None, nullable=False)
    library: Optional[Libraries] = Relationship(back_populates="items")
    itemAttachments: Optional[list["ItemAttachments"]] = Relationship(
        back_populates="item"
    )

    @classmethod
    def from_model(cls, model: Item) -> "Items":
        return cls(
            itemID=model.id,
        )

    def to_model(self) -> Item:
        return Item(
            id=self.itemID,
            key=self.key,
        )


class ItemAttachments(SQLModel, table=True):
    itemID: int = Field(primary_key=True, foreign_key="items.itemID")
    linkMode: int
    contentType: Optional[str]
    path: Optional[str]
    storageHash: Optional[str]
    item: Optional[Items] = Relationship(back_populates="itemAttachments")

    @classmethod
    def from_model(cls, model: File) -> "ItemAttachments":
        return cls(
            itemID=model.id,
            contentType=model.contentType,
            path=model.path,
        )

    def to_model(self) -> File:
        return File(
            id=self.itemID,
            contentType=self.contentType,
            path=self.path,
        )
