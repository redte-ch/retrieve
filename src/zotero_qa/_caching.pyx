# cython: language_level=3
# cython: c_string_type=unicode
# cython: c_string_encoding=utf8
# distutils: language=c++

import os

from msgspec import json

from cpython cimport bool
from libcpp.map cimport map
from libcpp.string cimport string

ctypedef map[string, int] CacheItem_t
ctypedef map[string, CacheItem_t] Cache_t


cdef public class Cache [object CyCache, type CyCache_t]:
    """A simple JSON cache for storing PDFs chuck sizes."""
    cdef public str path
    cdef public Cache_t cache

    def __cinit__(self, str path):
        self.path = path
        self.cache = Cache_t()

    cpdef void load(self):
        """Load or create the cache from/to disk."""
        if not os.path.exists(self.path):
            self.save()
        else:
            with open(self.path, "rb") as f:
                self.cache = Cache_t(json.decode(f.read()))

    cpdef void save(self):
        """Save the cache to disk."""
        with open(self.path, "wb") as f:
            f.write(json.encode(self.cache))

    cpdef CacheItem_t get(self, string key):
        """Retrieve value from cache."""
        if self.has_key(key):
            return self.cache[key]
        return CacheItem_t()

    cpdef void set(self, string key, CacheItem_t value):
        """Set value in cache and update the JSON file."""
        self.cache[key] = value

    cpdef bool has_key(self, string key):
        """Check if a key is already cached."""
        return self.cache.find(key) != self.cache.end()
