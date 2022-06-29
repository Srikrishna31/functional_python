load("@pytest//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])

py_test(
    name = "pytest_test",
    srcs = [
        "test_pytest.py",
    ],
    deps = [
        requirement("pytest")
        # "@dependencies_pytest_pytest//:pkg"
    ]
)
