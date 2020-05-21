
"""
This module explores various ways of applying map and filter functions
to sequences, iterables
"""
from typing import Callable, Any, Iterable, TypeVar, Tuple, Iterator
from chapters.working_with_collections.sequence_structure import group_by_iter
from math import sqrt as msqrt

T_ = TypeVar("T_")

def star_map(function: Callable[[Any], T_], *iterables: Iterable[Any]) -> Iterable[T_]:
    """
    A general map function, that takes n arguments of different types, and returns a single
    type as a result. This function returns an iterable, so that the memory consumption is
    preserved.wg
    """
    return (function(*args) for args in zip(*iterables))


def star_filter(function: Callable[[Any], bool], *iterables: Iterable[Any]) -> Iterable[Tuple[Any]]:
    """
    A general filter function, that takes n argument iterator, a predicate that returns true/false,
    and then only returns those iterable for which the predicate returned true.
    The return value is not exactly what we want, since we need to figure out a way to unzip the
    iterables so that a tuple of iterables is not returned.
    """
    return (args for args in zip(*iterables) if function(*args))


Point = Tuple[float, float]
Leg_Raw = Tuple[Point, Point]
Point_Func = Callable[[Point, Point], float]
Leg_P_D = Tuple[Leg_Raw, ...]


def cons_distance( distance: Point_Func, legs_iter: Iterable[Leg_Raw]) -> Iterator[Leg_P_D]:
    return (
        leg + (round(distance(*leg), 4),)   # 1-tuple
        for leg in legs_iter
    )


def group_filter_iter( n: int, pred: Callable[[Any], bool], items: Iterator) -> Iterator:
    subset = filter(pred, items)
    return group_by_iter(n, iter(subset))


def first(predicate: Callable[[Any], bool], collection: Iterable) -> Any:
    """
    This function applies a predicate to each value in the collection until it returns
    false. The moment the predicate returns true, the corresponding value will be returned
    without further processing the collection.
    """
    for x in collection:
        if predicate(x):
            return x

    return None


def isprimeh(x: int) -> bool:
    """
    This is a simple primality testing function, which demonstrates an application of
    the first function.
    """
    if x == 2: return True
    if x % 2 == 0: return False
    factor = first (
        lambda n: x % n == 0,
        range(3, int(msqrt(x) + .5)  + 1, 2))

    return factor is None


def map_not_none(func: Callable, source: Iterable) -> Iterator:
    """
    This function steps through the items in the iterable, assigning each item to the
    x variable. It attempts to apply the function to the item; if no exception is
    raised, the resulting value is yielded. If an exception is raised, the offending
    source item is silently dropped. Ofcourse, the exception details are print.
    This can be handy when dealing with data that include values that are not applicable
    or missing.
    """
    for x in source:
        try:
            yield func(x)
        except Exception as e:
            print(e)
