load("@dependencies_pytest//:requirements.bzl",
        _pytest_install = "pip_install",
        _mypy_install = "pip_install",
        _iniconfig_install = "pip_install")


def install_deps():
    _pytest_install()
    _mypy_install()
    _iniconfig_install()
