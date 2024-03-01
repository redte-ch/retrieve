# cython: language_level=3

import json
import os
from cpython cimport bool

cdef class Cache:
    """A simple JSON cache for storing PDFs chuck sizes."""

    cdef str _path
    cdef dict _cache

    def __cinit__(self, str path):
        self._path = path
        self._cache = self._load_cache()

    cpdef int get(self, str key):
        """Retrieve value from cache."""
        if self.has_key(key):
            return self._cache[key]
        return -1

    cpdef void set(self, str key, int value):
        """Set value in cache and update the JSON file."""
        self._cache[key] = value
        with open(self._path, "w") as f:
            json.dump(self._cache, f, indent=4)

    cpdef bool has_key(self, str key):
        """Check if a key is already cached."""
        return key in self._cache

    cdef dict _load_cache(self):
        """Load the cache from disk."""
        if os.path.exists(self._path):
            with open(self._path) as f:
                return json.load(f)
        else:
            return {}
