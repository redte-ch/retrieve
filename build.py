import shutil
from pathlib import Path

from setuptools import Extension
from setuptools.dist import Distribution
import Cython.Compiler.Options
from Cython.Build import (
    build_ext,
    cythonize,
)

Cython.Compiler.Options.annotate = True

extra_compile_args = [
    "-O3",
    "-Werror",
    "-Wno-unreachable-code-fallthrough",
    "-Wno-deprecated-declarations",
    "-Wno-parentheses-equality",
    "-UNDEBUG",
]


def dotted_path(path: Path) -> str:
    parts = path.parts

    if path.drive:
        return ".".join(parts[1:])

    return ".".join(parts)


def build_cython_extension(path: Path):
    extensions = [
        Extension(
            f"{dotted_path(path.parent)}.{path.stem}",
            [
                str(path),
            ],
            include_dirs=[str(path.parent)],
            extra_compile_args=extra_compile_args,
            language="c",
        ),
    ]

    include_dirs = set()
    for extension in extensions:
        include_dirs.update(extension.include_dirs)
    include_dirs = list(include_dirs)

    ext_modules = cythonize(
        extensions,
        include_path=include_dirs,
        language_level=3,
        annotate=True,
        compiler_directives={"linetrace": True, "binding": True},
        verbose=True,
    )
    dist = Distribution({"ext_modules": ext_modules})
    cmd = build_ext(dist)
    cmd.ensure_finalized()
    cmd.run()

    for output in cmd.get_outputs():
        output = Path(output)
        relative_extension = output.relative_to(cmd.build_lib)
        shutil.copyfile(output, relative_extension)


for path in Path("src/zotero_qa").rglob("*.pyx"):
    build_cython_extension(path)
