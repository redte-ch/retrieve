#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

import enum

import msgspec


class LibraryType(enum.StrEnum):
    USER = "user"
    GROUP = "group"


class Library(msgspec.Struct, frozen=True):
    """Represents a Zotero library."""

    id: int | None = msgspec.field(name="libraryID", default=None)
    type: str = LibraryType.USER
    editable: int = 1
    files_editable: int = msgspec.field(name="filesEditable", default=1)
    version: int = 0
    storage_version: int = msgspec.field(name="storageVersion", default=0)
    last_sync: int = msgspec.field(name="lastSync", default=0)
    archived: int = 0
    collections: list[Collection] = []
    groups: list[Group] = []
    items: list[Item] = []
    saved_searches: list[SavedSearch] = msgspec.field(name="savedSearches", default=[])
    storage_delete_log: list[StorageDeleteLog] = msgspec.field(
        name="storageDeleteLog", default=[]
    )
    sync_cache: list[SyncCache] = msgspec.field(name="syncCache", default=[])
    sync_queue: list[SyncQueue] = msgspec.field(name="syncQueue", default=[])
    synced_settings: list[SyncedSettings] = msgspec.field(
        name="syncedSettings", default=[]
    )

    def to_dict(self):
        return {f: getattr(self, f) for f in self.__struct_fields__}
