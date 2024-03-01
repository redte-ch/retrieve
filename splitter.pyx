"""Wrapper around the text splitter."""

import os

import dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load the environment variables.
dotenv.load_dotenv()

# The size of the chunks to split the text into.
chunk_size = int(os.getenv("CHUNK_SIZE"))

# The overlap between chunks.
chunk_overlap = int(os.getenv("CHUNK_OVERLAP"))


class Splitter(RecursiveCharacterTextSplitter):
    def __init__(self):
        super().__init__(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
