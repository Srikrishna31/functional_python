load ("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__pkg__"])

_IMPORTS = ["."]

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
    imports = _IMPORTS,
    srcs_version = "PY3",
)

_DEPS =  [
        ":working_with_collections",
        requirement("pytest")
    ]

_TESTS = [
    ":test_adjacent_pairer",
    ":test_basic_stats",
    ":test_kml_parser",
    ":test_sequence_structure"
]

py_test(
    name = "test_kml_parser",
    srcs = [
        "tests/test_kml_parser.py"
    ],
    imports = _IMPORTS,
    deps = _DEPS,
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
    imports = _IMPORTS,
    deps =_DEPS,
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
    imports = _IMPORTS,
    deps = _DEPS,
    visibility = ["//visibility:private"]
)

py_test(
    name = "test_sequence_structure",
    srcs = [
        "tests/test_sequence_structure.py"
    ],
    imports = _IMPORTS,
    deps = _DEPS,
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
