#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import msgspec

class Metadata:
    author: str
    created_at: str
    creator: str
    format: str
    keywords: str
    path: str
    producer: str
    subject: str
    title: str
    updated_at: str
    page: int
    total_pages: int
