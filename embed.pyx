"""Embed the documents in the vector store."""

import os

import dotenv

import helpers
from cache import Cache
from store import Store

# Load the environment variables.
dotenv.load_dotenv()

# The path to the Zotero storage directory.
zotero_path = os.getenv("ZOTERO_PATH")

# The directory to persist the vector store in.
db_path = os.getenv("DB_PATH")

# The vector store object.
store = Store()


def embed(max_chunks: int = 50) -> None:
    """Embed the documents in the vector store."""

    # The files to process.
    files = helpers.get_files(zotero_path)

    # The cache object.
    cache = Cache(f"{db_path}/cache.json")

    # Process the documents.
    for index, path in enumerate(files):
        # The filename of the document.
        filename = path.stem

        # The absolute path of the document.
        abspath = str(path)

        # The current progress.
        progress = f"{index + 1}/{len(files)}"

        # The current progress in percentage.
        percentage = f"{int((index + 1) * 100 / len(files))}%"

        # Check if the file has no documents (from cache).
        if cache.has_key(abspath) and cache.get(abspath) == 0:
            continue

        # Check if the file is too large (from cache).
        if cache.has_key(abspath) and cache.get(abspath) > max_chunks:
            continue

        print(f"Processing file {progress}: {abspath} ({percentage})")

        # Load the documents.
        docs = helpers.get_docs(abspath)

        # Check if there are any documents.
        if not docs:
            cache.set(abspath, 0)

        # Check again...
        if cache.get(abspath) == 0:
            print(f"    No documents found, skipping...")
            continue

        # Generate the ids.
        ids = helpers.get_ids(filename, docs)

        # Update the cache.
        cache.set(abspath, len(ids))

        # Check again...
        if cache.get(abspath) > max_chunks:
            print(f"    File to too large, skipping...")
            continue

        # Check if the file is already stored.
        if store.get(ids[0])["ids"]:
            print(f"    Already stored, skipping...")
            continue

        # Store the documents.
        helpers.store_docs(docs, ids, store.embedding)

        print(f"    Storing: OK!")
