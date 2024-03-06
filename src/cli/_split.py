#  Copyleft (?) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

import os

import rich
import rich.progress

import zotero_qa


def split(zotero_path: str, cache_path: str) -> None:
    if not zotero_path:
        raise ValueError("The path to the Zotero storage directory is required.")

    if not cache_path:
        raise ValueError("The path to the vector database directory is required.")

    rich.print("Getting the files to process...")
    paths = zotero_qa.list_files(f"{zotero_path}/storage")

    rich.print("Creating or loading the cache...")
    cache = zotero_qa.Cache(f"{cache_path}/cache.json")
    cache.load()

    print("Iterating over the files to split and store them in chunks...")
    for path in rich.progress.track(paths):
        # The absolute path to the document.
        abspath = str(path)

        # Check if the file is already in the cache.
        if cache.has_key(abspath) and cache.get(abspath)["split"] == 1:
            rich.print(f"Skipping: {abspath}...")
            continue

        # Check if the directory exists.
        if not os.path.exists(f"{cache_path}/splits"):
            os.makedirs(f"{cache_path}/splits")

        rich.print(f"Splitting: {abspath}...")
        doc = zotero_qa.open_file(abspath)

        # Get the ids.
        ids = zotero_qa.get_ids(abspath, doc)

        for i, page in enumerate(doc):
            # Store the chunk in a text file.
            with open(f"{cache_path}/splits/{ids[i].split('/')[-1]}.txt", "w") as f:
                f.write(page.text)

        rich.print(f"Storing splits: {abspath}...")
        cache.set(
            abspath, {"pages": cache.get(abspath)["pages"], "split": 1, "embedded": 0}
        )

    # Save the cache.
    rich.print("Saving to cache...")
    cache.save()
    rich.print("OK!")
