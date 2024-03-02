import shutil
from pathlib import Path
from setuptools import Extension, Distribution
from Cython.Build import build_ext, cythonize
import Cython.Compiler.Options as CompilerOptions

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
]

# Assuming that link arguments are the same as compile arguments for now.
# If there are link-specific arguments, they should be added here.
extra_link_args = extra_compile_args.copy()


def get_dotted_path(path: Path) -> str:
    """Convert a file system path to a dotted path notation used in Python modules."""
    # Skip the drive for Windows paths.
    parts = path.parts[1:] if path.drive else path.parts
    return ".".join(parts)


def build_cython_extension(source_path: Path):
    """Build a Cython extension from a given source file."""
    module_name = f"{get_dotted_path(source_path.parent)}.{source_path.stem}"
    extension = Extension(
        name=module_name,
        sources=[str(source_path)],
        include_dirs=[str(source_path.parent)],
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
        language="c",
    )

    ext_modules = cythonize(
        [extension],
        include_path=[str(source_path.parent)],
        language_level=3,
        annotate=True,
        compiler_directives={"linetrace": True, "binding": True},
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
for pyx_path in Path("src/zotero_qa").rglob("*.pyx"):
    build_cython_extension(pyx_path)
