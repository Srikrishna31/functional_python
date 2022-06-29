load("@dependencies_pytest//:requirements.bzl",
        _pytest_install = "install_deps",
        _import_coverage = "install_deps",
        _mypy_install = "install_deps")


def install_deps():
    _pytest_install()
    _mypy_install()
    _import_coverage()
