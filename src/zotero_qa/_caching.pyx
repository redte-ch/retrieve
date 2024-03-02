# cython: language_level=3

import json
import os

from cpython cimport bool


cdef class Cache:
    """A simple JSON cache for storing PDFs chuck sizes."""

    cdef str path
    cdef dict cache

    def __cinit__(self, str path):
        self.path = path
        self.cache = self.load_cache()

    cpdef int get(self, str key):
        """Retrieve value from cache."""

        if self.has_key(key):
            return self.cache[key]

        return -1

    cpdef void set(self, str key, int value):
        """Set value in cache and update the JSON file."""

        cdef str path = self.path
        cdef str mode = "w"
        self.cache[key] = value

        with open(path, mode) as f:
            json.dump(self.cache, f, indent=4)

    cpdef bool has_key(self, str key):
        """Check if a key is already cached."""

        return key in self.cache

    cdef dict load_cache(self):
        """Load the cache from disk."""

        cdef str path = self.path

        if os.path.exists(path):
            with open(path) as f:
                return json.load(f)

        else:
            return {}
