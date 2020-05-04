"""
This module contains two implementations of functions that accept iterable of
any type, and return a generator that provides pairs of adjacent elements.
More formally:
Given a sequence, S = {s0, s1, s2, ... , sn}, we would also want to create a
paired sequence, S` = {(s0,s1), (s1,s2), (s2,s3), ... , (sn-1, sn)}.
A paired sequence will allow us to use each pair to compute distances from
point to point using a trivial application of a haversine function.
"""

from typing import Iterator, Any, Tuple, TypeVar

T_ = TypeVar("T_")
Item_Iter = Iterator[T_]
Pairs_Iter = Iterator[Tuple[T_, T_]]

def pairs_recursive(iterator: Item_Iter) -> Pairs_Iter:
    def pair_from(
        head: Any,
        iterable_tail: Item_Iter) -> Pairs_Iter:

        nxt = next(iterable_tail)
        yield head, nxt
        yield from pair_from(nxt, iterable_tail)

    try:
        return pair_from(next(iterator), iterator)
    except StopIteration:
        return iter([])


def pairs(iterator: Item_Iter) -> Pairs_Iter:
    begin = next(iterator)
    for end in iterator:
        yield begin, end
        begin = end