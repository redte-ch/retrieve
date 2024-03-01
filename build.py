from Cython.Build import cythonize

compiler_directives = {"language_level": 3, "embedsignature": True}


def build(setup_kwargs):
    setup_kwargs.update(
        {
            "name": "zotero-qa",
            "package": ["zotero_qa"],
            "ext_modules": cythonize(
                module_list="src/zotero_qa/**/*.pyx",
                compiler_directives=compiler_directives,
                nthreads=5,
            ),
        },
    )
