#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import msgspec


class Page(msgspec.Struct, frozen=True):
    """Represents a page with text and page number."""

    # The text content of the page
    text: str

    # The page number
    page: int


class Document(msgspec.Struct, frozen=True):
    """Represents a document with metadata and content."""

    # The author of the document
    author: str

    # The creation date of the document
    created_at: str

    # The creator of the document
    creator: str

    # The format of the document
    format: str

    # Keywords associated with the document
    keywords: str

    # The content page of the document
    page: Page

    # The file path of the document
    path: str

    # The producer of the document
    producer: str

    # The subject of the document
    subject: str

    # The title of the document
    title: str

    # The total number of pages in the document
    total_pages: int

    # The last update date of the document
    updated_at: str
