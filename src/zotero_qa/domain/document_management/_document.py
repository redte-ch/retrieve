#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import msgspec


class Author(msgspec.Struct, frozen=True):
    """Represents an author."""

    # The name of the author
    first_name: str

    # The last name of the author
    last_name: str


class Document(msgspec.Struct, frozen=True):
    """Represents a document with metadata and content."""

    # The author of the document
    authors: list[Author]

    # The title of the document
    title: str

    # The publication date of the document
    date: int

    # The summary of the document
    summary: str

    # The content of the document
    content: str

    def __eq__(self, other: object) -> bool:
        if not (
            hasattr(other, "authors")
            and hasattr(other, "title")
            and hasattr(other, "date")
        ):
            return False

        return (
            hasattr(other, "authors")
            and hasattr(other, "title")
            and hasattr(other, "date")
            and self.authors == getattr(other, "authors")
            and self.title == getattr(other, "title")
            and self.date == getattr(other, "date")
        )
