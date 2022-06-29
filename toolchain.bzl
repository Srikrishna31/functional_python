load("@rules_python//python:defs.bzl", "py_runtime")

def python3():
    py_runtime(
        name = "python3",
        interpreter_path = "C:\Users\coolk\AppData\Local\Programs\Python\Python310"
    )
