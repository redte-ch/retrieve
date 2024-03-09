#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

from typing import Protocol, Sequence, TypeVar

T = TypeVar("T")


class Model(Protocol):
    id: int | None


class ORM(Protocol):
    @staticmethod
    def from_model(__model: Model) -> ORM: ...
    def to_model(self, __exclude: ORM | None = ...) -> Model: ...


class Repo(Protocol[T]):
    def add(self, __instance: T) -> None: ...
    def get(self, __id: int) -> T | None: ...
    def list(self) -> Sequence[T]: ...
