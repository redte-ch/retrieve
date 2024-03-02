# cython: language_level=3
# cython: c_string_type=unicode
# cython: c_string_encoding=utf8


cdef struct Metadata:
    char* author
    char* creationDate
    char* creator
    char* file_path
    char* format
    char* keywords
    char* modDate
    int page
    char* producer
    char* source
    char* subject
    char* title
    int total_pages
    char* trapped


cdef struct Document:
    char* text
    Metadata metadata
