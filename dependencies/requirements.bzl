load("@rules_python//python:pip.bzl", "pip_import")


#TODO: Write a rule in bazel to download the python interpreter and then run the code.
interpreter_path = "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe"


def load_deps():
    # Create a central repo that knows about the dependencies needed for
    # requirements.txt.
    _import_mypy()
    _import_pytest()


def _import_pytest():
        pip_import(   # or pip3_import
        name = "dependencies_pytest",
        requirements = "//dependencies/pytest:requirements.txt",
        python_interpreter = interpreter_path
    )


def _import_mypy():
        pip_import(   # or pip3_import
        name = "dependencies_mypy",
        requirements = "//dependencies/mypy:requirements.txt",
        python_interpreter = interpreter_path
    )
