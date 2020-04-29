load("@dependencies_pytest//:requirements.bzl", "requirement")

py_library(
    name = "func_iter_gen",
    srcs = [
        "__init__.py",
        "power.py",
        "prime_factors.py"
    ],
    srcs_version = "PY3"
)

py_test(
    name = "test_power",
    srcs = [
        "tests/test_power.py",
    ],
    deps = [
        ":func_iter_gen",
        requirement("pytest")
    ]
)


py_test(
    name = "test_prime_factors",
    srcs = [
        "tests/test_prime_factors.py"
    ],
    deps = [
        ":func_iter_gen",
        requirement("pytest")
    ]
)
