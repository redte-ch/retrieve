#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

#  cython: language_level=3

"""Wrapper around the vector store."""

import os

import dotenv
from chromadb import Client
from chromadb.config import Settings
from langchain.text_splitter import Document
from langchain_community.vectorstores import Chroma

from zotero_qa.embeddings import Embeddings

# Load the environment variables.
dotenv.load_dotenv()

# The name of the Ollama model to use.
model_name = os.getenv('MODEL_NAME')

# The name of the collection to store the documents in.
db_name = os.getenv('DB_NAME')

# The directory to persist the vector store in.
db_path = os.getenv('DB_PATH')

# The embedding function to use.
embeddings = Embeddings(model_name)


class Store(Chroma):
    """The vector store."""

    def __init__(
        self,
        collection_name: str = db_name,
        persist_directory: str = db_path,
        embedding_function: Embeddings = embeddings,
        client_settings: Settings = None,
        client: Client = None,
        collection_metadata: dict = None,
    ) -> None:
        super().__init__(
            collection_name=collection_name,
            persist_directory=persist_directory,
            embedding_function=Embeddings(model_name),
            client_settings=client_settings,
            client=client,
            collection_metadata=collection_metadata,
        )
        self.embedding = self._embedding_function

    def from_docs(self, docs: list[Document], ids: list[str]) -> Chroma:
        """Load store from documents."""
        return self.__class__.from_documents(
            ids=ids,
            documents=docs,
            embedding=self.embedding,
            collection_name=db_name,
            persist_directory=db_path,
        )
