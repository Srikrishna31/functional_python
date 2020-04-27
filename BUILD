load("@dependencies_pytest//:requirements.bzl", "requirement")

py_library(
    name = "func_iter_gen",
    srcs = [
        "functions_iterators_generators/power.py",
        "functions_iterators_generators/__init__.py"
    ],
    srcs_version = "PY3"
)

py_test(
    name = "test_power",
    srcs = [
        "functions_iterators_generators/tests/test_power.py"
    ],
    deps = [
        ":func_iter_gen",
        requirement("pytest")
    ]
)