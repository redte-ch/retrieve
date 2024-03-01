"""Helper functions for the project."""

import os
from pathlib import Path

import dotenv
from langchain.text_splitter import Document
from langchain_community.document_loaders import PyPDFLoader

from store import Store
from text_splitter import TextSplitter

# Load the environment variables.
dotenv.load_dotenv()

# The path to the Zotero storage directory.
zotero_path = os.getenv("ZOTERO_PATH")

# The name of the Ollama model to use.
model_name = os.getenv("MODEL_NAME")

# The size of the chunks to split the text into.
chunk_size = int(os.getenv("CHUNK_SIZE"))

# The overlap between chunks.
chunk_overlap = int(os.getenv("CHUNK_OVERLAP"))

# The vector store object.
store = Store()

# The text splitter object.
splitter = TextSplitter(chunk_size, chunk_overlap)


def get_files(path: str) -> list[Path]:
    """Recursively find all PDF files in a directory."""
    print(f"Finding PDF files in: {zotero_path}")
    directory = Path(path)
    return list(directory.rglob("*.pdf"))


def get_docs(path: str) -> list[Document]:
    """Load a document from the file system."""
    print("    Loading...")
    data = PyPDFLoader(path).load()
    return splitter.split_documents(data)


def get_ids(path: str, docs: list[Document]) -> list[str]:
    """Generate the IDs for the documents."""
    print("    Generating IDs...")
    return [f"{path.replace(' ', '_')}_{index + 1}" for index, doc in enumerate(docs)]


def store_docs(docs: list[Document], ids: list[str]) -> None:
    """Store a document in the vector store."""
    print("    Storing documents...")
    store.from_docs(docs, ids).persist()
