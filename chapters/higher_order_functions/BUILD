load ("@dependencies_pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//chapters:__pkg__"])

_MODULE = "higher_order_functions"

_TESTS = [
    "test_min_max"
]


py_library(
    name = _MODULE,
    srcs = [
        "min_max.py"
    ],
    imports = ["."],
    srcs_version = "PY3",
    deps = [
        "//chapters/working_with_collections",
    ]
)


[
    py_test(
        name = "%s" %(n),
        srcs = [
            "tests/%s.py" %(n),
        ],
        imports = ["."],
        deps = [
            ":%s" %(_MODULE),
            requirement("pytest")
        ]
    )
    for n in _TESTS
]


test_suite(
    name = "test_%s"%(_MODULE),
)