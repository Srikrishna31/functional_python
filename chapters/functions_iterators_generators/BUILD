load("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__pkg__"])

_MODULE = "functions_iterators_generators"

py_library(
    name = "functions_iterators_generators",
    srcs = [
        "__init__.py",
        "power.py",
        "prime_factors.py",
        "static_mapping.py",
    ],
    imports=["."],
    srcs_version = "PY3",
)

_TESTS = [
    "test_power",
    "test_prime_factors",
    "test_static_mapping"
]

[
py_test(
    name = "%s" %(n),
    srcs = [
        "tests/%s.py" %(n),
    ],
    imports = ["."],
    deps = [
        ":%s"%(_MODULE),
        requirement("pytest")
    ],
    visibility = ["//visibility:private"]
) for n in _TESTS
]

test_suite(
    name = "test_%s" %(_MODULE),
)
