# cython: language_level=3
# cython: c_string_type=unicode
# cython: c_string_encoding=utf8
# Based on https://github.com/langchain-ai/langchain.

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
    cdef object doc
    cdef public char* path
    cdef int total_pages

    def __cinit__(self, char* path):
        """Initialize with a file path."""
        self.doc = fitz.open(path)
        self.path = path
        self.total_pages = self.doc.page_count


cdef class PageParser:
    """Parse a PDF document page."""
    cdef DocLoader loader
    cdef object doc

    def __cinit__(self, DocLoader loader):
        """Initialize the parser."""
        self.loader = loader
        self.doc = loader.doc

    cpdef Page parse(self, int at):
        """Parse the doc."""
        cdef str page_text = self.loader.doc.get_page_text(at - 1)
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
                total_pages=self.loader.total_pages,
                updated_at=metadata.get("modDate", ""),
            )
        )
