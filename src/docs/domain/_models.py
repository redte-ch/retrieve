#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

import enum
from dataclasses import dataclass, field


class LibraryType(enum.StrEnum):
    USER = "user"
    GROUP = "group"


@dataclass(frozen=True)
class Library:
    id: int | None = None
    type: str = LibraryType.USER
    editable: int = 0
    filesEditable: int = 0
    collections: list[Collection] = field(default_factory=list)
    items: list[Item] = field(default_factory=list)


@dataclass(frozen=True)
class Collection:
    id: int | None = None
    name: str | None = None
    collection_id: int | None = None
    library_id: int | None = None
    key: str | None = None
    library: Library | None = None
    items: list[Item] = field(default_factory=list)


@dataclass(frozen=True)
class Item:
    id: int | None = None
    type_id: int | None = None
    library_id: int | None = None
    key: str | None = None
    library: Library | None = None
    collections: list[Collection] = field(default_factory=list)
    files: list[File] = field(default_factory=list)


@dataclass(frozen=True)
class File:
    id: int | None = None
    path: str | None = None
    link_mode: int | None = None
    content_type: str | None = None
    storage_hash: str | None = None
    item: Item | None = None
