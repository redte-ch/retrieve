"""Wrapper around the vector store."""

import os

import dotenv
from langchain.text_splitter import Document
from langchain_community.vectorstores import Chroma

from embeddings import Embeddings

# Load the environment variables.
dotenv.load_dotenv()

# The name of the Ollama model to use.
model_name = os.getenv("MODEL_NAME")

# The name of the collection to store the documents in.
db_name = os.getenv("DB_NAME")

# The directory to persist the vector store in.
db_path = os.getenv("DB_PATH")


class Store(Chroma):
    """The vector store."""

    def __init__(self):
        self.embedding = Embeddings(model_name)
        super().__init__(
            collection_name=db_name,
            persist_directory=db_path,
            embedding_function=self.embedding,
        )

    def from_docs(self, docs: list[Document], ids: list[str]) -> Chroma:
        """Load store from documents."""
        self.__class__.from_documents(
            ids=ids,
            documents=docs,
            embedding=self.embedding,
            collection_name=db_name,
            persist_directory=db_path,
        )
