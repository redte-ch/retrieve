#  Inspired by https://github.com/langchain-ai/langchain.
#
#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

#  cython: language_level=3
#  cython: c_string_type=unicode
#  cython: c_string_encoding=utf8

"""Load and parse a PDF document using MuPDF."""

import fitz

from .domain._document import Metadata, Page


class DocLoader:
    """Load a PDF document from a file path."""

    doc: fitz.Document
    path: str

    def __init__(self, path: str) -> None:
        """Initialize with a file path."""
        self.doc = fitz.open(path, filetype="pdf")
        self.path = path


class PageParser:
    """Parse a PDF document page."""

    loader: DocLoader
    doc: fitz.Document

    def __init__(self, loader: DocLoader) -> None:
        """Initialize the parser."""
        self.loader = loader
        self.doc = self.loader.doc

    def parse(self, at: int) -> Page:
        """Parse the doc."""
        page_text: str = self.doc.get_page_text(at - 1).rstrip("\n")
        metadata: dict[str, int | str] = self.doc.metadata

        return Page(
            text=page_text,
            metadata=Metadata(
                author=metadata.get("author", ""),
                created_at=metadata.get("creationDate", ""),
                creator=metadata.get("creator", ""),
                format=metadata.get("format"),
                keywords=metadata.get("keywords", ""),
                page=at,
                path=self.loader.path,
                producer=metadata.get("producer", ""),
                subject=metadata.get("subject", ""),
                title=metadata.get("title"),
                total_pages=self.doc.page_count,
                updated_at=metadata.get("modDate", ""),
            ),
        )
