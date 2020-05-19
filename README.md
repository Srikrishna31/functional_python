# Motivation
This project explores the functional programming techniques that are possible in Python, by following the book Functional Python Programming.
Some of the concepts explored:
1. Writing generator functions which model the lazy evaluation - rather than materialize the entire sequence, the values can be queried one at a time.
2. Using type annotations to improve the reasoning ability of the code, and also have mypy do a static analysis of the code.


# Setup
This project uses rules_python to properly setup dependencies like pytest and other frameworks. More on this here: https://github.com/bazelbuild/rules_python

# Organization
The code is organized as follows:
    1. WORKSPACE and top level BUILD files - designate the project related items.
    2. chapters module - This is the core of the project, where any new chapter module will be added. Each chapter contains certain aspects of python, that have been explored.
    3. dependencies - Any third party dependencies needed by the modules. Eg., the tests use pytest, so it is one of the dependencies.
    4. .gitignore file describing the artifacts to be ignored from consideration to adding into the repository.
    5. .gitattributes file describing the line ending settings for the files.

# Specifying Third Party Dependencies
The way to specify dependencies is:
1. Create a folder with the respective dependency name, and add requirements.txt to it. Optionally, a test specifying the success of the import can also be specified.
2. In requirements.bzl, add a function with the "dependencies_"<dependency> name, and provide path to the requirements.txt file to be downloaded.
3. In setup.bazel, load the "dependencies_"<dependency>//:requirements.bzl (created by rules_python module), and alias the pip_install function to the dependency install function.
4. Then in the install_deps() function, add a call in the end for the dependency.
5. In the BUILD file, load the "dependencies_"<dependency>//:requirements.bzl, "requirement" function, and in the deps attribute, specify as <requirement("dependency")>.

# Adding a new chapter module
1. Make folder with appropriate name in chapters module, and add __init__.py
2. Create a build file for the module, and add a py_library target, and as many py_test targets as needed.
3. Finally, group all the py_test targets into a testsuite, so that they can be referenced from the chapters module.
4. In the chapters' BUILD file, add the module dependency to py_library, and add the testsuite target in the tests attribute of the global test suite.
5. Then do bazel build functional_python, bazel test test_functional_python and verify that the newly added module is building and it's tests are executing.
