load("@rules_python//python:pip.bzl", "pip_import")


def load_deps():
    # Create a central repo that knows about the dependencies needed for
    # requirements.txt.
    pip_import(   # or pip3_import
        name = "dependencies_pytest",
        requirements = "//dependencies/pytest:requirements.txt",
        #TODO: Specify the path once, may be in the workspace and refer it from there.
        python_interpreter = "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe"
    )
