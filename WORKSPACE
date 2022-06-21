workspace(name = "functional_python")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
http_archive(
    name = "rules_python",
    sha256 = "5fa3c738d33acca3b97622a13a741129f67ef43f5fdfcec63b29374cc0574c29",
    strip_prefix = "rules_python-0.9.0",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/0.9.0.tar.gz",
)

load("@rules_python//python:defs.bzl", "py_test", "py_binary", "py_library", "py_runtime")

# Load the central repo's install function from its `//:requirements.bzl` file,
# and call it.
load("//dependencies:requirements.bzl", "load_deps")
load_deps()

load("//dependencies:setup.bzl", "install_deps")
install_deps()
