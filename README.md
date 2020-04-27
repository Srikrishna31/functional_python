# Motivation
This project explores the functional programming techniques that are possible in Python, by following the book Functional Python Programming.

# Setup
This project uses rules_python to properly setup dependencies like pytest and other frameworks.

# Specifying Third Party Dependencies
The way to specify dependencies is:
1. Create a folder with the respective dependency name, and add requirements.txt to it. Optionally, a test specifying the success of the import can also be specified.
2. In requirements.bzl, add a function with the "dependencies_"<dependency> name, and provide path to the requirements.txt file to be downloaded.
3. In setup.bazel, load the "dependencies_"<dependency>//:requirements.bzl (created by rules_python module), and alias the pip_install function to the dependency install function.
4. Then in the install_deps() function, add a call in the end for the dependency.
5. In the BUILD file, load the "dependencies_"<dependency>//:requirements.bzl, "requirement" function, and in the deps attribute, specify as <requirement("dependency")>.
