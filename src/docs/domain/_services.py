#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Sequence

from ._models import Item, File


def get_pdf_paths(items: list[Item], base_path: str) -> Sequence[str]:
    pdf_paths = []

    for item in items:
        for file in item.files:
            if _is_pdf(file) and not _is_orphan(file):
                storage_path, file_path = file.path.split(":")
                pdf_paths.append(f"{base_path}/{storage_path}/{item.key}/{file_path}")

    return pdf_paths


def _is_pdf(file: File) -> bool:
    return file.contentType == "application/pdf" and file.path is not None


def _is_orphan(file: File) -> bool:
    return file.id is None
