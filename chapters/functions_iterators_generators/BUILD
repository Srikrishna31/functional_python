load("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__pkg__"])

py_library(
    name = "func_iter_gen",
    srcs = [
        "__init__.py",
        "power.py",
        "prime_factors.py",
        "static_mapping.py",
    ],
    srcs_version = "PY3",
)

py_test(
    name = "test_power",
    srcs = [
        "tests/test_power.py",
    ],
    deps = [
        ":func_iter_gen",
        requirement("pytest")
    ],
    visibility = ["//visibility:private"]
)


py_test(
    name = "test_prime_factors",
    srcs = [
        "tests/test_prime_factors.py"
    ],
    deps = [
        ":func_iter_gen",
        requirement("pytest")
    ],
    visibility = ["//visibility:private"]
)

py_test(
    name = "test_static_mapping",
    srcs = [
        "tests/test_static_mapping.py"
    ],
    deps = [
        ":func_iter_gen",
        requirement("pytest")
    ],
    visibility = ["//visibility:private"]
)

test_suite(
    name = "test_functions_iterators_generators",
    tests = [
        ":test_power",
        ":test_prime_factors",
        ":test_static_mapping"
    ],
)
