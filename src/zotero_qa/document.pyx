# cython: language_level=3

cdef class Document:
    cdef public str page_content
    cdef public dict metadata

    def __init__(self, str page_content, dict metadata):
        self.page_content = page_content
        self.metadata = metadata
