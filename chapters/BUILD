

py_library(
    name = "functional_python",
    srcs = [
        "__init__.py",
    ],
    srcs_version = "PY3",
    deps = [
        "//chapters/functions_iterators_generators:func_iter_gen",
        "//chapters/higher_order_functions",
        "//chapters/working_with_collections",

    ]
)

test_suite(
    name = "test_functional_python",
    tests = [
        "//chapters/functions_iterators_generators:test_functions_iterators_generators",
        "//chapters/higher_order_functions:test_higher_order_functions",
        "//chapters/working_with_collections:test_working_with_collections",
    ]
)
