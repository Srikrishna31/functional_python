workspace(name = "functional_python")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "a0fbf98d4e3a232144df4d0d80b577c7a693b570",
    shallow_since = "1586444447 +0200",
)

load("@rules_python//python:defs.bzl", "py_test", "py_binary", "py_library", "py_runtime")

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()
load("@rules_python//python:pip.bzl", "pip_repositories")
pip_repositories()

# Load the central repo's install function from its `//:requirements.bzl` file,
# and call it.
load("//dependencies:requirements.bzl", "load_deps")
load_deps()

load("//dependencies:setup.bzl", "install_deps")
install_deps()

