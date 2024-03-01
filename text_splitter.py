import os
from typing import Iterable

import dotenv
from langchain.text_splitter import Document, RecursiveCharacterTextSplitter

# Load the environment variables.
dotenv.load_dotenv()

# The size of the chunks to split the text into.
chunk_size = int(os.getenv("CHUNK_SIZE"))

# The overlap between chunks.
chunk_overlap = int(os.getenv("CHUNK_OVERLAP"))


class TextSplitter:
    """Wrapper around the text splitter."""

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )

    def split_documents(self, docs: Iterable[Document]) -> list[Document]:
        """Split a list of documents into chunks."""
        texts, metadatas = [], []
        for doc in docs:
            texts.append(doc.page_content)
            metadatas.append(doc.metadata)
        return self.splitter.create_documents(texts, metadatas=metadatas)
