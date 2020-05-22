"""
This module explores some recursion functions,
and also the non-recursive equivalents.
It also demonstrates where it is beneficial to
leave the recursion as is.
"""


def factorial_recursive(n: int) -> int:
    if n == 0: return 1
    else: return n * factorial_recursive(n - 1)


def factorial_imperative(n: int) -> int:
    if n == 0: return 1
    f = 1
    for i in range(2, n):
        f = f * i

    return f
