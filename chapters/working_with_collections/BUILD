load ("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__pkg__"])

py_library(
    name="working_with_collections",
    srcs = [
        "adjacent_pairer.py",
        "basic_stats.py",
        "haversine.py",
        "__init__.py",
        "kml_parser.py",
        "sequence_structure.py"
    ],
    srcs_version = "PY3",
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
        "//chapters/working_with_collections/data:kml_files",
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
        "//chapters/working_with_collections/data:kml_files",
    ],
    visibility = ["//visibility:private"]
)

py_test(
    name = "test_basic_stats",
    srcs = [
        "tests/test_basic_stats.py"
    ],
    deps = [
        ":working_with_collections",
        requirement("pytest")
    ],
    visibility = ["//visibility:private"]
)

py_test(
    name = "test_sequence_structure",
    srcs = [
        "tests/test_sequence_structure.py"
    ],
    deps = [
        ":working_with_collections",
        requirement("pytest")
    ],
    visibility = ["//visibility:private"]
)

test_suite(
    name="test_working_with_collections",
    tests = [
        ":test_adjacent_pairer",
        ":test_basic_stats",
        ":test_kml_parser",
        ":test_sequence_structure"
    ]
)