#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

#  cython: language_level=3

from zotero_qa cimport Page, PageParser


cdef class DocSplitter:
    cpdef list[Page] split(self, PageParser parser, TextSplitter text_splitter)


cdef class TextSplitter:
    cdef public int chunk_size
    cdef public int chunk_overlap
    cdef char* separator
    cdef object separator_pattern

    cpdef list[char*] split(self, char* text)
    cpdef list[char*] merge(self, list[char*] splits)
    cdef list[char*] get_current_chunk(self, list current_chunk)
    cdef int get_current_len(self, list[char*] current_chunk)
