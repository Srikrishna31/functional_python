"""
This module explores some recursion functions,
and also the non-recursive equivalents.
It also demonstrates where it is beneficial to
leave the recursion as is.
"""
from typing import Callable, Sequence, Any, Iterable, Iterator, TypeVar, List

def factorial_recursive(n: int) -> int:
    if n == 0: return 1
    else: return n * factorial_recursive(n - 1)


def factorial_imperative(n: int) -> int:
    if n == 0: return 1
    f = 1
    for i in range(2, n+1):
        f = f * i

    return f


def fast_power(a: float, n: int) -> float:
    if n == 0:
        return 1
    if n % 2 == 1:
        return a * fast_power(a, n - 1)

    t = fast_power(a, n // 2)
    return t * t


def fib_recursive(n : int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_imperative(n : int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    f_n2, f_n1 = 1, 1

    for _ in range(3, n+1):
        f_n2, f_n1 = f_n1, f_n2 + f_n1

    return f_n1


def map_recursive(f: Callable[[Any], Any], collection: Sequence[Any]) -> List[Any]:
    if len(collection) == 0: return []
    return map_recursive(f, collection[:-1]) + [f(collection[-1])]



T = TypeVar("T")
U = TypeVar("U")


def map_imperative(f: Callable[[T], U], C: Iterable[T]) -> Iterator[U]:
    return (f(x) for x in C)


