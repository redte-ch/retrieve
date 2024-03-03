# cython: language_level=3

"""Load and parse a PDF document using MuPDF."""


cdef struct Metadata:
    char* path


cdef struct Page:
    Metadata metadata


cdef class DocLoader:
    cdef public char* path

cdef class PageParser:
    cpdef Page parse(self, int at)
