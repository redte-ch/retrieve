"""Helper functions for the project."""

import os
from pathlib import Path

import dotenv
import numpy
from langchain_community.document_loaders import PyMuPDFLoader

from zotero_qa cimport Document
from zotero_qa.store import Store
from zotero_qa.text_splitter import TextSplitter

# It's necessary to call "import_array" if you use any part of the
# numpy PyArray_* API. From Cython 3, accessing attributes like
# ".shape" on a typed Numpy array use this API. Therefore we recommend
# always calling "import_array" whenever you "cimport numpy".
#
# Source: https://cython.readthedocs.io/en/latest/src/tutorial/numpy.html
# numpy.import_array()

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
splitter = TextSplitter(chunk_size, chunk_overlap, "\n\n")


def get_files(path: str) -> list[Path]:
    """Recursively find all PDF files in a directory."""
    print(f"Finding PDF files in: {zotero_path}")
    directory = Path(path)
    return list(directory.rglob("*.pdf"))


def get_docs(path: str) -> list[Document]:
    """Load a document from the file system."""
    print("    Loading...")
    data = PyMuPDFLoader(path).load()
    shape = len(data)
    array = numpy.empty([shape], dtype=object)

    for index in range(shape):
        array[index] = data[index]

    return splitter.split_documents(data)


def get_ids(path: str, docs: list[Document]) -> list[str]:
    """Generate the IDs for the documents."""
    print("    Generating IDs...")
    return [f"{path.replace(' ', '_')}_{index + 1}" for index, doc in enumerate(docs)]


def store_docs(docs: list[Document], ids: list[str]) -> None:
    """Store a document in the vector store."""
    print("    Storing documents...")
    store.from_docs(docs, ids).persist()
