#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

from typing import Protocol, Sequence


class Model(Protocol): ...


class ORM(Protocol):
    @staticmethod
    def from_model(__model: Model) -> ORM: ...
    def to_model(self) -> Model: ...


class Repo(Protocol):
    def add(self, __instance: Model) -> None: ...
    def get(self, __id: int) -> Model | None: ...
    def list(self) -> Sequence[Model]: ...
