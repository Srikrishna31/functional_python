

py_library(
    name = "functional_python",
    srcs = [
        "__init__.py",
    ],
    imports = ["."],
    srcs_version = "PY3",
    deps = [
        "//chapters/functions_iterators_generators:functions_iterators_generators",
        "//chapters/higher_order_functions:higher_order_functions",
        "//chapters/recursions_and_reductions:recursions_and_reductions",
        "//chapters/working_with_collections:working_with_collections",
    ],
    visibility = [
        "//:__pkg__",
        "//examples:__pkg__"
    ]
)

test_suite(
    name = "test_functional_python",
    tests = [
        "//chapters/functions_iterators_generators:test_functions_iterators_generators",
        "//chapters/higher_order_functions:test_higher_order_functions",
        "//chapters/recursions_and_reductions:test_recursions_and_reductions",
        "//chapters/working_with_collections:test_working_with_collections",
    ],
    visibility = ["//:__pkg__"]
)
