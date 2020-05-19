from typing import TypeVar, Sequence, List, Tuple, Iterator

ItemType = TypeVar("ItemType")
Flat = Sequence[ItemType]
Flat_Iter = Iterator[ItemType]
Grouped = List[Tuple[ItemType, ...]]
Grouped_Iter = Iterator[Tuple[ItemType, ...]]

"""
This module explores some functions through which, a flat
sequence can be bunched up into subgroups.
"""

def group_by_seq(n: int, sequence: Flat) -> Grouped:
    """
    Given a flat sequence of values, and an integer n, this
    function groups n values together, and returns another
    sequence of tuples containing elements together.
    If there is any left over elements in the end, they
    will be grouped together, which contain less than n
    elements.
    """
    flat_iter = iter(sequence)
    full_sized_items = list(tuple(next(flat_iter)
        for _ in range(n))
            for _ in range(len(sequence) // n))

    trailer = tuple(flat_iter)

    return full_sized_items + [trailer] if trailer else full_sized_items


def group_by_iter(n: int, iterable: Flat_Iter) -> Grouped_Iter:
    """
    Given an iterable sequence, and an integer n, returns a
    Grouped Iterable, which provides a tuple of n values together.
    """
    row = tuple(next(iterable) for _ in range(n))
    while row:
        yield row
        row = tuple(next(iterable) for _ in range(n))


def group_by_seq_alternative(n: int, sequence: Flat) -> Grouped_Iter:
    """
    This function provides an alternative approach, using the zip
    function provided by python.
    Note that, since this function uses zip internally, the final
    items will not be part of the result, i.e they will be truncated.
    """
    return zip(*(sequence[i::n] for i in range(n)))


def digits(x: int, b: int) -> Iterator[int]:
    """
    Given a number and its base, this function returns
    an iterator that produces the digits of the number
    in that base. Note that there is no error checking
    if the number confirms to the base. The behavior
    would be undefined, if it is not the case.
    """
    if x == 0: return
    yield x % b
    for d in digits (x // b, b):
        yield d


def reversed_digits(x: int, b: int) -> Iterator[int]:
    """
    Given a number ant its base, this function returns
    an iterator that produces the digits of the number
    in that base in reverse order.
    """
    return reversed(tuple(digits(x,b)))

