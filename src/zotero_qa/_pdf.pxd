# cython: language_level=3

"""Load and parse a PDF document using MuPDF."""


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
    cdef public object doc
    cdef public char* path


cdef class PageParser:
    cdef public DocLoader loader
    cdef public object doc
    cpdef Page parse(self, int at)
