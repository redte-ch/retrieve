"""Build Cython extensions from .pyx files using the distutils module."""

import os
import shutil
import sys
from pathlib import Path

import Cython.Compiler.Options as CompilerOptions
import numpy
from Cython.Build import build_ext, cythonize
from dotenv import dotenv_values
from setuptools import Distribution, Extension

# Set the file or glob pattern to build Cython extensions from.
glob = sys.argv[1:] and sys.argv[1] or "*.pyx"

# Load environment variables from the .env file.
env = dotenv_values(".env")

# Force the use of the C++ compiler for all Cython code.
os.environ["CC"] = env["CC"]
os.environ["CPP"] = env["CPP"]
os.environ["CXX"] = env["CXX"]

# Enable annotation in Cython for performance analysis.
CompilerOptions.annotate = True

# Compiler and linker arguments for optimization and warnings.
extra_compile_args = [
    "-O3",  # Optimize code, more aggressive level of optimization.
    "-Wall",  # Enable all warning messages.
    "-Werror",  # Treat warnings as errors.
    "-fopenmp",  # Enable OpenMP for parallel programming.
    "-march=native",  # Optimize for the architecture of the compiling machine.
    "-mtune=native",  # Tune the code for the architecture of the compiling machine.
    "-Wno-error=address",  # Disable address sanitizer warnings.
]

extra_link_args = [
    "-fopenmp",  # Enable OpenMP for parallel programming.
]


def get_dotted_path(path: Path) -> str:
    """Convert a file system path to a dotted path notation used in Python modules."""
    # Skip the drive for Windows paths.
    parts = path.parts[1:] if path.drive else path.parts
    return ".".join(parts)


def build_cython_extension(source_path: Path):
    """Build a Cython extension from a given source file."""
    module_name = f"{get_dotted_path(source_path.parent)}.{source_path.stem}"
    # Define an extension module.
    extension = Extension(
        name=module_name,
        sources=[str(source_path)],
        include_dirs=[str(source_path.parent), numpy.get_include()],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        extra_link_args=extra_link_args,
        extra_compile_args=extra_compile_args,
    )

    # Use cythonize to compile the Cython source file(s) into C extension modules.
    ext_modules = cythonize(
        # List of extension objects to be compiled.
        [extension],
        # Directories to search for .pxd files.
        include_path=[str(source_path.parent)],
        # Python language level to interpret the source code.
        language_level=3,
        # Generate HTML annotation file to visualize code translation.
        annotate=True,
        compiler_directives={
            # Enable line tracing for coverage reporting.
            "linetrace": False,
            # Prepare the code for profiling.
            "profile": False,
            # Allow C functions to be called with Python call semantics.
            "binding": True,
        },
        # Print detailed compilation information.
        verbose=True,
    )

    dist = Distribution({"ext_modules": ext_modules})
    cmd = build_ext(dist)
    cmd.ensure_finalized()
    cmd.run()

    # Copy built extensions to their source directories.
    for output in cmd.get_outputs():
        target_path = Path(output).relative_to(cmd.build_lib)
        shutil.copy(output, target_path)


# Build Cython extensions for all .pyx files in a specific directory.
for pyx_path in Path("src").rglob(glob):
    build_cython_extension(pyx_path)
