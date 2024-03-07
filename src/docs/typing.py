#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from __future__ import annotations

from typing import Protocol, Sequence, TypeVar

Model = TypeVar("Model")

Engine = TypeVar("Engine")


class Repo(Protocol[Model]):
    # The actual db we'll use.
    engine: Engine

    def __init__(self, __engine: Engine) -> None: ...
    def add(self, __instance: Model) -> None: ...
    def get(self, __id: int) -> Model | None: ...
    def list(self) -> Sequence[Model]: ...
