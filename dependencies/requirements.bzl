load("@rules_python//python:pip.bzl", "pip_parse")


#TODO: Write a rule in bazel to download the python interpreter and then run the code.
interpreter_path = "C:/Users/coolk/AppData/Local/Programs/Python/Python310/python.exe"


def load_deps():
    # Create a central repo that knows about the dependencies needed for
    # requirements.txt.
    _import_mypy()
    _import_pytest()
    _import_coverage()


def _import_pytest():
    pip_parse(   # or pip3_import
        name = "dependencies_pytest",
        requirements_lock = "//dependencies/pytest:requirements.txt",
        python_interpreter = interpreter_path
    )

def _import_mypy():
    pip_parse(   # or pip3_import
        name = "dependencies_mypy",
        requirements_lock = "//dependencies/mypy:requirements.txt",
        python_interpreter = interpreter_path
    )

def _import_coverage():
    pip_parse(
        name = "dependencies_coverage",
        requirements_lock = "//dependencies/coverage:requirements.txt",
        python_interpreter = interpreter_path
    )
