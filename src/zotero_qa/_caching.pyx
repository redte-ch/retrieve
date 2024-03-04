# cython: language_level=3
# cython: c_string_type=unicode
# cython: c_string_encoding=utf8
# distutils: language = c++

import os

import ujson

from cpython cimport bool
from libcpp.map cimport map
from libcpp.string cimport string

ctypedef map[string, int] Cache_t


cdef class Cache:
    """A simple JSON cache for storing PDFs chuck sizes."""
    cdef public str path
    cdef public Cache_t cache

    def __cinit__(self, str path):
        self.path = path
        self.cache = Cache_t()

    def __init__(self, str path):
        self.path = path
        self.cache = Cache_t()

    cpdef void load(self):
        """Load or create the cache from/to disk."""
        if not os.path.exists(self.path):
            self.save()
        else:
            with open(self.path, "r") as f:
                self.cache = Cache_t(ujson.loads(f.read()))

    cpdef void save(self):
        """Save the cache to disk."""
        with open(self.path, "w") as f:
            f.write(ujson.dumps(self.cache))

    cpdef int get(self, string key):
        """Retrieve value from cache."""
        if self.has_key(key):
            return self.cache[key]
        return -1

    cpdef void set(self, string key, int value):
        """Set value in cache and update the JSON file."""
        self.cache[key] = value

    cpdef bool has_key(self, string key):
        """Check if a key is already cached."""
        return self.cache.find(key) != self.cache.end()
