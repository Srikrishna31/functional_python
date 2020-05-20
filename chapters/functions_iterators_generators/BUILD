load("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__pkg__"])

IMPORTS = ["."]

py_library(
    name = "functions_iterators_generators",
    srcs = [
        "__init__.py",
        "power.py",
        "prime_factors.py",
        "static_mapping.py",
    ],
    imports=IMPORTS,
    srcs_version = "PY3",
)

DEPS = [
    ":functions_iterators_generators",
    requirement("pytest")
]

py_test(
    name = "test_power",
    srcs = [
        "tests/test_power.py",
    ],
    imports = IMPORTS,
    deps = DEPS,
    visibility = ["//visibility:private"]
)


py_test(
    name = "test_prime_factors",
    srcs = [
        "tests/test_prime_factors.py"
    ],
    imports = IMPORTS,
    deps = DEPS,
    visibility = ["//visibility:private"]
)

py_test(
    name = "test_static_mapping",
    srcs = [
        "tests/test_static_mapping.py"
    ],
    imports = IMPORTS,
    deps = DEPS,
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
