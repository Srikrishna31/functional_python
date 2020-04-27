load("@rules_python//python:defs.bzl", "py_runtime")

def python3():
    py_runtime(
        name = "python3",
        interpreter_path = "C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64"
    )