#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12
#
#  cython: language_level=3
#  cython: c_string_type=unicode
#  cython: c_string_encoding=utf8

"""Helper functions for the project."""

import os
from pathlib import Path

import dotenv

from zotero_qa cimport DocLoader, DocSplitter, Page, PageParser, TextSplitter

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
cdef str zotero_path = str(os.getenv("ZOTERO_PATH"))

# The name of the Ollama model to use.
cdef str model_name = str(os.getenv("MODEL_NAME"))

# The size of the chunks to split the text into.
cdef int chunk_size = int(os.getenv("CHUNK_SIZE"))

# The overlap between chunks.
cdef int chunk_overlap = int(os.getenv("CHUNK_OVERLAP"))

# The separator to use when joining the chunks.
cdef str separator = str(os.getenv("SEPARATOR"))

# The vector store object.
# store = Store()

# The text splitter object.
# splitter = TextSplitter(chunk_size, chunk_overlap, "\n\n")


cpdef list[char*] list_files(char* path):
    """Recursively find all PDF files in a directory."""
    cdef list[char*] pdf_files = []
    cdef list[char*] files
    cdef list[char*] dirs
    cdef char* file
    cdef char* root

    print(f"Finding PDF files in: {path}")

    # Walk the directory tree
    for root, dirs, files in os.walk(path):
        for file in files:
            # Check if the file ends with .pdf
            if file.endswith(".pdf"):
                # Construct the full path to the file
                full_path = os.path.join(root, file)
                # Add the full path to the list of PDF files
                pdf_files.append(full_path)

    return pdf_files


cpdef list[Page] open_file(str path):
    """Load and parse a PDF file."""
    cdef DocLoader loader = DocLoader(path)
    cdef PageParser parser = PageParser(loader)
    cdef DocSplitter doc_splitter = DocSplitter()
    cdef TextSplitter text_splitter = TextSplitter(
        chunk_size,
        chunk_overlap,
        separator,
    )

    print("    Loading...")

    return doc_splitter.split(parser, text_splitter)
#
#
# def get_ids(path: str, docs: list[Document]) -> list[str]:
#     """Generate the IDs for the documents."""
#     print("    Generating IDs...")
#     return [f"{path.replace(' ', '_')}_{index + 1}" for index, doc in enumerate(docs)]
#
#
# def store_docs(docs: list[Document], ids: list[str]) -> None:
#     """Store a document in the vector store."""
#     print("    Storing documents...")
#     store.from_docs(docs, ids).persist()
