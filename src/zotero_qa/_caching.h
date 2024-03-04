/* Generated by Cython 3.0.8 */

#ifndef __PYX_HAVE__src__zotero_qa___caching
#define __PYX_HAVE__src__zotero_qa___caching

#include "Python.h"
struct CyCache;

/* "src/zotero_qa/_caching.pyx":17
 * 
 * 
 * cdef public class Cache [object CyCache, type CyCache_t]:             # <<<<<<<<<<<<<<
 *     """A simple JSON cache for storing PDFs chuck sizes."""
 *     cdef public str path
 */
struct CyCache {
  PyObject_HEAD
  struct __pyx_vtabstruct_3src_9zotero_qa_8_caching_Cache *__pyx_vtab;
  PyObject *path;
  __pyx_t_3src_9zotero_qa_8_caching_Cache_t cache;
};

#ifndef __PYX_HAVE_API__src__zotero_qa___caching

#ifdef CYTHON_EXTERN_C
    #undef __PYX_EXTERN_C
    #define __PYX_EXTERN_C CYTHON_EXTERN_C
#elif defined(__PYX_EXTERN_C)
    #ifdef _MSC_VER
    #pragma message ("Please do not define the '__PYX_EXTERN_C' macro externally. Use 'CYTHON_EXTERN_C' instead.")
    #else
    #warning Please do not define the '__PYX_EXTERN_C' macro externally. Use 'CYTHON_EXTERN_C' instead.
    #endif
#else
    #define __PYX_EXTERN_C extern "C++"
#endif

#ifndef DL_IMPORT
  #define DL_IMPORT(_T) _T
#endif

__PYX_EXTERN_C DL_IMPORT(PyTypeObject) CyCache_t;

#endif /* !__PYX_HAVE_API__src__zotero_qa___caching */

/* WARNING: the interface of the module init function changed in CPython 3.5. */
/* It now returns a PyModuleDef instance instead of a PyModule instance. */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init_caching(void);
#else
/* WARNING: Use PyImport_AppendInittab("_caching", PyInit__caching) instead of calling PyInit__caching directly from Python 3.5 */
PyMODINIT_FUNC PyInit__caching(void);

#if PY_VERSION_HEX >= 0x03050000 && (defined(__GNUC__) || defined(__clang__) || defined(_MSC_VER) || (defined(__cplusplus) && __cplusplus >= 201402L))
#if defined(__cplusplus) && __cplusplus >= 201402L
[[deprecated("Use PyImport_AppendInittab(\"_caching\", PyInit__caching) instead of calling PyInit__caching directly.")]] inline
#elif defined(__GNUC__) || defined(__clang__)
__attribute__ ((__deprecated__("Use PyImport_AppendInittab(\"_caching\", PyInit__caching) instead of calling PyInit__caching directly."), __unused__)) __inline__
#elif defined(_MSC_VER)
__declspec(deprecated("Use PyImport_AppendInittab(\"_caching\", PyInit__caching) instead of calling PyInit__caching directly.")) __inline
#endif
static PyObject* __PYX_WARN_IF_PyInit__caching_INIT_CALLED(PyObject* res) {
  return res;
}
#define PyInit__caching() __PYX_WARN_IF_PyInit__caching_INIT_CALLED(PyInit__caching())
#endif
#endif

#endif /* !__PYX_HAVE__src__zotero_qa___caching */