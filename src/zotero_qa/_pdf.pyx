# cython: language_level=3
# cython: c_string_type=unicode
# cython: c_string_encoding=utf8
# Based on https://github.com/langchain-ai/langchain.

from pathlib import Path
from typing import Iterator

import fitz

from zotero_qa cimport Document, Metadata


class PDFLoader:
    """Load `PDF` files using `PyMuPDF`."""

    file_path: str
    source: str

    def __init__(self, path: Path) -> None:
        """Initialize with a file path."""
        self.file_path = str(path)
        self.source = self.file_path

    def load(self) -> fitz.Document:
        """Load file."""
        return fitz.open(self.file_path, filetype="pdf")


class PDFParser:
    """Parse `PDF` using `PyMuPDF`."""

    def __init__(self, loader: PDFLoader) -> None:
        """Initialize the parser."""
        self.loader = loader
        self.doc = loader.load()

    def parse(self) -> Iterator[Document]:
        """Parse the doc."""
        yield from [
            Document(
                text=page.get_text().strip().replace("\n \n", "\n\n"),
                metadata=Metadata(
                    author=self.doc.metadata["author"],
                    creationDate=self.doc.metadata["creationDate"],
                    creator=self.doc.metadata["creator"],
                    file_path=self.loader.source,
                    format=self.doc.metadata["format"],
                    keywords=self.doc.metadata["keywords"],
                    modDate=self.doc.metadata["modDate"],
                    page=page.number,
                    producer=self.doc.metadata["producer"],
                    source=self.loader.source,
                    subject=self.doc.metadata["subject"],
                    title=self.doc.metadata["title"],
                    total_pages = self.doc.page_count,
                )
            )
            for page in self.doc
        ]
