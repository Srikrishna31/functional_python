load ("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__subpackages__"])

_MODULE = "recursions_and_reductions"

py_library(
    name=_MODULE,
    srcs = [
        "recursions.py",
    ],
    imports = ["."],
    srcs_version = "PY3",
)


_TESTS = [
    "test_recursions"
]


[
py_test(
    name = "%s" %(n),
    srcs = [
        "tests/%s.py" %(n)
    ],
    imports = ["."],
    deps = [
        ":%s"%(_MODULE),
        requirement("pytest")
    ],
    visibility = ["//visibility:private"]
)
for n in _TESTS
]


test_suite(
    name="test_%s"%(_MODULE),
)
