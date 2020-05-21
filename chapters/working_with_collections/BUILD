load ("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__subpackages__"])

_MODULE = "working_with_collections"

py_library(
    name=_MODULE,
    srcs = [
        "adjacent_pairer.py",
        "basic_stats.py",
        "haversine.py",
        "__init__.py",
        "kml_parser.py",
        "sequence_structure.py"
    ],
    imports = ["."],
    srcs_version = "PY3",
)


_TESTS = [
    "test_adjacent_pairer",
    "test_basic_stats",
    "test_kml_parser",
    "test_sequence_structure"
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
        "//chapters/working_with_collections/data:kml_files",
    ],
    visibility = ["//visibility:private"]
)
for n in _TESTS
]


test_suite(
    name="test_%s"%(_MODULE),
)
