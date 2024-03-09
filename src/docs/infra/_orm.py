#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from docs.domain import Collection, File, Item, Library


class CollectionItems(SQLModel, table=True):
    collectionID: int = Field(primary_key=True, foreign_key="collections.collectionID")
    itemID: int = Field(primary_key=True, foreign_key="items.itemID")
    orderIndex: int = Field(default=0)


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

    def to_model(self, exclude: Optional[SQLModel] = None) -> Library:
        return Library(
            id=self.libraryID,
            type=self.type,
            editable=self.editable,
            filesEditable=self.filesEditable,
            collections=tuple(
                [
                    collection.to_model(exclude=self)
                    for collection in self.collections
                    if collection != exclude
                ]
                if self.collections is not None
                else ()
            ),
            items=tuple(
                [item.to_model(exclude=self) for item in self.items if item != exclude]
                if self.items is not None
                else ()
            ),
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
    items: Optional[list["Items"]] = Relationship(
        back_populates="collections", link_model=CollectionItems
    )

    @classmethod
    def from_model(cls, model: Collection) -> "Collections":
        return cls(
            collectionID=model.id,
            collectionName=model.name,
            parentCollectionID=model.collection_id,
            libraryID=model.library_id,
            key=model.key,
        )

    def to_model(self, exclude: Optional[SQLModel] = None) -> Collection:
        return Collection(
            id=self.collectionID,
            name=self.collectionName,
            collection_id=self.parentCollectionID,
            library_id=self.libraryID,
            key=self.key,
            library=(
                self.library.to_model(exclude=self)
                if self.library is not None and self.library != exclude
                else None
            ),
            items=tuple(
                [item.to_model(exclude=self) for item in self.items if item != exclude]
                if self.items is not None
                else ()
            ),
        )


class Items(SQLModel, table=True):
    itemID: int = Field(primary_key=True)
    itemTypeID: int = Field(default=None, nullable=False)
    libraryID: int = Field(
        default=None, foreign_key="libraries.libraryID", nullable=False
    )
    key: str = Field(default=None, nullable=False)
    library: Optional[Libraries] = Relationship(back_populates="items")
    collections: Optional[list["Collections"]] = Relationship(
        back_populates="items", link_model=CollectionItems
    )
    itemAttachments: Optional[list["ItemAttachments"]] = Relationship(
        back_populates="item"
    )

    @classmethod
    def from_model(cls, model: Item) -> "Items":
        return cls(
            itemID=model.id,
            itemTypeID=model.type_id,
            libraryID=model.library_id,
            key=model.key,
        )

    def to_model(self, exclude: Optional[SQLModel] = None) -> Item:
        return Item(
            id=self.itemID,
            type_id=self.itemTypeID,
            library_id=self.libraryID,
            key=self.key,
            library=(
                self.library.to_model(exclude=self)
                if self.library is not None and self.library != exclude
                else None
            ),
            collections=tuple(
                [
                    collection.to_model(exclude=self)
                    for collection in self.collections
                    if collection != exclude
                ]
                if self.collections is not None
                else ()
            ),
            files=tuple(
                [
                    file.to_model(exclude=self)
                    for file in self.itemAttachments
                    if file != exclude
                ]
                if self.itemAttachments is not None
                else ()
            ),
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
            path=model.path,
            linkMode=model.link_mode,
            contentType=model.content_type,
            storageHash=model.storage_hash,
        )

    def to_model(self, exclude: Optional[SQLModel] = None) -> File:
        return File(
            id=self.itemID,
            path=self.path,
            link_mode=self.linkMode,
            content_type=self.contentType,
            storage_hash=self.storageHash,
            item=(
                self.item.to_model(exclude=self)
                if self.item is not None and self.item != exclude
                else None
            ),
        )
