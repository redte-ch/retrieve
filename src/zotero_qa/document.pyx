# cython: language_level=3

cdef class Document:
    def __cinit__(self, str page_content, dict metadata):
        self.page_content = page_content.encode("utf-8").decode("utf-8")
        self.metadata = metadata
