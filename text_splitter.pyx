import copy
import re
from typing import Iterable

from document import Document


class TextSplitter:
    """Wrapper around the text splitter."""

    def __init__(self, chunk_size: int, chunk_overlap: int) -> None:
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        # Pre-compile the regular expression for performance
        self.separator_pattern = re.compile(re.escape("\n\n"))

    def split_text(self, text: str) -> list[str]:
        """Split incoming text into chunks based on chunk_size and separator."""
        # Split text using the compiled regex
        splits = self.separator_pattern.split(text)
        # Filter out any empty strings
        splits = [s for s in splits if s]
        # Merge splits into chunks based on chunk_size and chunk_overlap
        return self._merge_splits(splits)

    def split_documents(self, docs: Iterable[Document]) -> list[Document]:
        """Split a list of documents into chunks, preserving metadata."""
        result_docs = []
        for doc in docs:
            for chunk in self.split_text(doc.page_content):
                # Use copy to ensure metadata is not shared between chunks
                new_doc = Document(
                    page_content=chunk, metadata=copy.deepcopy(doc.metadata)
                )
                result_docs.append(new_doc)
        return result_docs

    def _merge_splits(self, splits: list[str]) -> list[str]:
        """Merge splits into chunks, respecting the chunk_size and chunk_overlap."""
        chunks = []
        current_chunk = []
        current_len = 0

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
