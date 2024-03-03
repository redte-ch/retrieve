# cython: language_level=3

from zotero_qa cimport Page, PageParser


cdef class DocSplitter:
    cpdef list[Page] split(self, PageParser parser, TextSplitter text_splitter)


cdef class TextSplitter:
    cdef public int chunk_size
    cdef public int chunk_overlap
    cpdef list[char*] split(self, char* text)
    cpdef list[char*] merge(self, list[char*] splits)
