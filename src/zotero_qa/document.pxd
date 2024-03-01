# cython: language_level=3

cdef class Document:
    cdef public str page_content
    cdef public dict metadata
