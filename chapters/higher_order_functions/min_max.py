from typing import Iterator, Iterable, Tuple, Any, TextIO, Callable
from  chapters.working_with_collections import kml_parser as kp

"""
This module explores some ways to use the min and max functions,
and also defines custom max_like and min_like functions that take
a callable to do custom processing.
"""
Wrapped = Tuple[Any, Tuple]


def wrap(leg_iter: Iterable[Tuple]) -> Iterable[Wrapped]:
    return ((leg[2], leg) for leg in leg_iter)


def unwrap(dist_leg: Tuple[Any, Any]) -> Any:
    _, leg = dist_leg
    return leg


def max_like(source: TextIO, key: Callable = lambda x : x) -> Any:
    wrp = ((key(leg), leg) for leg in kp.trip(source))
    return sorted(wrp)[-1][1]


def min_like(source: TextIO, key: Callable = lambda x : x) -> Any:
    wrp = ((key(leg), leg) for leg in kp.trip(source))
    return sorted(wrp, reverse=True)[-1][1]


def long(source: TextIO) -> kp.LL_Float:
    return unwrap(max(wrap(kp.trip(source))))


def short(source: TextIO) -> kp.LL_Float:
    return unwrap(min(wrap(kp.trip(source))))
