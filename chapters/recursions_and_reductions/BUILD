load ("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__subpackages__"])

_MODULE = "recursions_and_reductions"

py_library(
    name=_MODULE,
    srcs = [
        "file_parsers.py",
        "recursions.py",
        "reductions.py",
    ],
    imports = ["."],
    srcs_version = "PY3",
)


_TESTS = [
    "test_recursions",
    "test_reductions",
    "test_file_parsers"
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
    data = [
        "//chapters/%s/data:palette_files"%(_MODULE)
    ],
    visibility = ["//visibility:private"]
)
for n in _TESTS
]


test_suite(
    name="test_%s"%(_MODULE),
)
