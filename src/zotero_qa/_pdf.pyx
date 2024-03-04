#  Inspired by https://github.com/langchain-ai/langchain.
#
#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
#
#  cython: language_level=3
#  cython: c_string_type=unicode
#  cython: c_string_encoding=utf8

"""Load and parse a PDF document using MuPDF."""

import fitz


cdef struct Metadata:
    char* author
    char* created_at
    char* creator
    char* format
    char* keywords
    char* path
    char* producer
    char* subject
    char* title
    char* updated_at
    int page
    int total_pages


cdef struct Page:
    char* text
    Metadata metadata


cdef class DocLoader:
    """Load a PDF document from a file path."""
    cdef public object doc
    cdef public char* path

    def __cinit__(self, char* path):
        """Initialize with a file path."""
        self.doc = fitz.open(path, filetype="pdf")
        self.path = path


cdef class PageParser:
    """Parse a PDF document page."""
    cdef public DocLoader loader
    cdef public object doc

    def __cinit__(self, DocLoader loader):
        """Initialize the parser."""
        self.loader = loader
        self.doc = self.loader.doc

    cpdef Page parse(self, int at):
        """Parse the doc."""
        cdef str page_text = self.doc.get_page_text(at - 1)
        cdef dict metadata = self.doc.metadata

        return Page(
            text=page_text.strip().replace("\n \n", "\n\n"),
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
            )
        )
