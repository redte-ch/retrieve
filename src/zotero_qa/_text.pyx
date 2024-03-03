# cython: language_level=3
# cython: c_string_type=unicode
# cython: c_string_encoding=utf8

import re

from zotero_qa cimport Page, PageParser


cdef class DocSplitter:
    cpdef list[Page] split(self, PageParser parser, TextSplitter text_splitter):
        cdef int n = parser.doc.page_count
        cdef list[Page] acc = []

        for i in range(n):
            page = parser.parse(i + 1)
            text = page.text
            split = text_splitter.split(text)
            merged = text_splitter.merge(split)

            for chunk in merged:
                new = Page(text=chunk, metadata=page.metadata)
                acc.append(new)

        return acc


cdef class TextSplitter:
    cdef public int chunk_size
    cdef public int chunk_overlap
    cdef char* separator
    cdef object separator_pattern

    def __cinit__(self, int chunk_size, int chunk_overlap, char* separator):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separator = separator
        self.separator_pattern = re.compile(re.escape(separator))

    cpdef list[char*] split(self, char* text):
        # Split text using the compiled regex
        cdef list[str] splits = self.separator_pattern.split(text)

        # Filter out any empty strings
        return [s for s in splits if s]

    cpdef list[char*] merge(self, list[char*] splits):
        cdef list[char*] chunks = []
        cdef list[char*] current_chunk = []
        cdef int current_len = 0
        cdef int split_len
        cdef int separator_len = len(self.separator)

        for split in splits:
            split_len = len(split)
            # Check if adding this split would exceed the chunk_size
            # Update to include the separator length in the calculation
            if (
                current_len
                + split_len
                + (separator_len * (len(current_chunk) if current_chunk else 0))
                > self.chunk_size
            ):
                # If current_chunk is not empty, add it to chunks
                if current_chunk:
                    chunks.append(self.separator.join(current_chunk))
                    # Start a new chunk considering chunk_overlap
                    current_chunk = self.get_current_chunk(current_chunk)
                    current_len = self.get_current_len(current_chunk)
            current_chunk.append(split)
            # Update current_len: add split_len + length of a separator for each
            # split after the first.
            current_len += split_len + (
                separator_len if current_chunk[:-1] else 0
            )  # Add separator length if not the first split in chunk

        # Add the last chunk if it's not empty
        if current_chunk:
            chunks.append(self.separator.join(current_chunk))

        return chunks

    cdef list[char*] get_current_chunk(self, list current_chunk):
        """Get the current chunk considering chunk_overlap."""
        if self.chunk_overlap:
            return current_chunk[-self.chunk_overlap :]
        return []

    cdef int get_current_len(self, list[char*] current_chunk):
        """Calculate the length of the current chunk."""
        return sum(len(part) for part in current_chunk) + len(self.separator) * (
            len(current_chunk) - 1 if current_chunk else 0
        )
