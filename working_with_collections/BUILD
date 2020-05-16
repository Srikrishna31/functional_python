load ("@dependencies_pytest//:requirements.bzl", "requirement")

py_library(
    name="working_with_collections",
    srcs = [
        "adjacent_pairer.py",
        "haversine.py",
        "__init__.py",
        "kml_parser.py",
    ],
    srcs_version = "PY3"
)

py_test(
    name = "test_kml_parser",
    srcs = [
        "tests/test_kml_parser.py"
    ],
    deps = [
        ":working_with_collections",
        requirement("pytest")
    ],
    data = [
        "//working_with_collections/data:kml_files",
    ],
    visibility = ["//visibility:private"]
)

py_test(
    name = "test_adjacent_pairer",
    srcs = [
        "tests/test_adjacent_pairer.py"
    ],
    deps = [
        ":working_with_collections",
        requirement("pytest")
    ],
    data = [
        "//working_with_collections/data:kml_files",
    ],
    visibility = ["//visibility:private"]
)


test_suite(
    name="test_working_with_collections",
    tests = [
        ":test_adjacent_pairer",
        ":test_kml_parser"
    ]
)