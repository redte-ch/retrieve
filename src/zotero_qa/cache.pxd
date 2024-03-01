# cython: language_level=3

from cpython cimport bool


cdef class Cache:
    cpdef int get(self, str key)
    cpdef void set(self, str key, int value)
    cpdef bool has_key(self, str key)
