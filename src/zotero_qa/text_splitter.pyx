# cython: language_level=3
# cython: c_string_type=unicode
# cython: c_string_encoding=utf8

import copy
import re

from document cimport Document


cdef class TextSplitter:
    cdef int chunk_size
    cdef int chunk_overlap
    cdef public object separator_pattern

    cpdef list[Document] split_documents(self, list[Document] docs):
        cdef list result_docs = []
        cdef str chunk
        cdef Document doc
        for d in docs:
            for chunk in self.split_text(d.page_content):
                # Use copy to ensure metadata is not shared between chunks
                doc = Document(page_content=chunk, metadata=copy.deepcopy(d.metadata))
                result_docs.append(doc)
        return result_docs

    def __cinit__(self, int chunk_size, int chunk_overlap, char* separator):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separator_pattern = re.compile(re.escape(separator))

    cpdef list[str] split_text(self, char* text):
        # Split text using the compiled regex
        cdef list[str] splits = self.separator_pattern.split(text)
        # Filter out any empty strings
        splits = [s for s in splits if s]
        # Merge splits into chunks based on chunk_size and chunk_overlap
        return self.merge_splits(splits)

    cdef list[char*] merge_splits(self, list[char*] splits):
        cdef list[char*] chunks = []
        cdef list[char*] current_chunk = []
        cdef int current_len = 0
        cdef int split_len

        for split in splits:
            split_len = len(split)
            # Check if adding this split would exceed the chunk_size
            if current_len + split_len > self.chunk_size:
                # If current_chunk is not empty, add it to chunks
                if current_chunk:
                    chunks.append("\n\n".join(current_chunk))
                    # Start a new chunk considering chunk_overlap
                    current_chunk = (
                        current_chunk[-self.chunk_overlap :]
                        if self.chunk_overlap
                        else []
                    )
                    current_len = (
                        sum(len(part) for part in current_chunk)
                        + len(current_chunk)
                        - 1
                    )
            current_chunk.append(split)
            current_len += (len(current_chunk) - 1 if current_chunk else 0) + split_len

        # Add the last chunk if it's not empty
        if current_chunk:
            chunks.append("\n\n".join(current_chunk))

        return chunks
