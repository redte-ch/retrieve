#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import rich
import rich.progress

import retrievals


def cache(zotero_path: str, cache_path: str) -> None:
    """Cache some of the Zotero library's metadata.

    Parsing and embedding the Zotero library's page numbers into the database
    is a time-consuming process. This command allows to cache the files' page
    numbers first to speed up the process.

    Args:
        zotero_path (str): The path to the Zotero storage directory.
        cache_path (str): The directory to persist the cache in.

    Returns:
        None

    """

    if not zotero_path:
        raise ValueError("The path to the Zotero storage directory is required.")

    if not cache_path:
        raise ValueError("The path to the vector database directory is required.")

    rich.print("Getting the files to process...")
    paths = retrievals.list_files(f"{zotero_path}/storage")

    rich.print("Creating or loading the cache...")
    cache = retrievals.Cache(f"{cache_path}/cache.json")
    cache.load()

    print("Iterating over the files to cache their page numbers...")
    for path in rich.progress.track(paths):
        # The absolute path to the document.
        abspath = str(path)

        # Check if the file is already in the cache.
        if cache.has_key(abspath):
            rich.print(f"Skipping: {abspath}...")
            continue

        # Load the document.
        doc = retrievals.DocLoader(abspath).doc

        rich.print(f"Caching: {abspath}...")
        cache.set(abspath, {"pages": doc.page_count, "split": 0, "embedded": 0})

    # Save the cache.
    rich.print("Saving to cache...")
    cache.save()
    rich.print("OK!")
