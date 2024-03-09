#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

from typing import Sequence


import enum

from dataclasses import dataclass


class LibraryType(enum.StrEnum):
    USER = "user"
    GROUP = "group"


@dataclass(frozen=True)
class Library:
    id: int | None = None
    type: str = LibraryType.USER
    editable: int = 0
    filesEditable: int = 0


@dataclass(frozen=True)
class Collection:
    id: int | None = None


@dataclass(frozen=True)
class Item:
    id: int | None = None
    key: str | None = None
    files: Sequence[File] = tuple()



@dataclass(frozen=True)
class File:
    id: int | None = None
    contentType: str | None = None
    path: str | None = None
