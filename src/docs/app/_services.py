#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Sequence, TypeGuard

from docs.domain import File, Item
from docs.typing import Repo


def get_pdf_paths(base_path: str, repo: Repo[Item]) -> Sequence[str]:
    items = repo.list()
    pdf_paths = []

    for item in items:
        for file in item.files:
            if _is_valid(file) and _is_str(path := file.path):
                storage_path, file_path = path.split(":")
                pdf_paths.append(f"{base_path}/{storage_path}/{item.key}/{file_path}")

    return pdf_paths


def _is_valid(file: File) -> bool:
    return file.id is not None and file.content_type == "application/pdf"


def _is_str(path: object) -> TypeGuard[str]:
    return isinstance(path, str)
