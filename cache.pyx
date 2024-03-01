"""Cache to avoid loading each text every time."""

import json
import os


class Cache:
    """A simple JSON cache for storing PDFs chuck sizes."""

    def __init__(self, path: str) -> None:
        self.path = path
        self.cache = self._load_cache()

    def get(self, key: str) -> int | None:
        """Retrieve value from cache."""
        return self.cache.get(key)

    def set(self, key: str, value: int) -> None:
        """Set value in cache and update the JSON file."""
        self.cache[key] = value
        with open(self.path, "w") as f:
            json.dump(self.cache, f, indent=4)

    def has_key(self, key: str) -> bool:
        """Check if a key is already cached."""
        return key in self.cache

    def _load_cache(self) -> dict[str, int | str]:
        """Load the cache file from disk."""
        if os.path.exists(self.path):
            with open(self.path) as f:
                return json.load(f)
        else:
            return {}
