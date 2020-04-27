workspace(name = "functional_python")

load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "a0fbf98d4e3a232144df4d0d80b577c7a693b570",
    shallow_since = "1586444447 +0200",
)

# load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
# http_archive(
#     name = "rules_python",
#     url = "https://github.com/bazelbuild/rules_python/releases/download/0.0.1/rules_python-0.0.1.tar.gz",
#     sha256 = "aa96a691d3a8177f3215b14b0edc9641787abaaa30363a080165d06ab65e1161",
# )

load("@rules_python//python:defs.bzl", "py_test", "py_binary", "py_library", "py_runtime")
# load("//:toolchain.bzl", "python3")
# python3()

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()
# Only needed if using the packaging rules.
load("@rules_python//python:pip.bzl", "pip_repositories")
pip_repositories()



# Load the central repo's install function from its `//:requirements.bzl` file,
# and call it.
# load("@my_deps//:requirements.bzl", "pip_install")
# pip_install()

load("//dependencies:requirements.bzl", "load_deps")
load_deps()

load("//dependencies:setup.bzl", "install_deps")
install_deps()

