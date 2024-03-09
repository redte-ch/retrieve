#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

from typing import Sequence

from docs import domain
from docs.domain import Item
from docs.typing import Repo


def get_pdf_paths(base_path: str, repo: Repo[Item]) -> Sequence[str]:
    return domain.get_pdf_paths(repo.list(), base_path)
