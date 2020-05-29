from typing import Dict, Any, Iterable, Tuple, List, TypeVar, Callable, Sequence
from collections import defaultdict
Leg = Tuple[Any, Any, float]
T_ = TypeVar("T_")

def group_sort(trip: Iterable[Leg]) -> Dict[int, int]:
    def group( data: Iterable[T_]) -> Iterable[Tuple[T_, int]]:
        sorted_data = iter(sorted(data))
        value, count = next(sorted_data), 1
        for cur in sorted_data:
            if cur == value:
                count += 1
            else:
                yield value, count
                value, count = cur, 1

        yield previous, count

    quantized = (int(5*(dist // 5)) for beg, end, dist in trip)

    return dict(group(quantized))


S = TypeVar("S")
K = TypeVar("K")


def group_by_recursive(key: Callable[[S], K], data: Sequence[S]) -> Dict[K, List[S]]:
    """
    This is a general group by reduction function, which, given a collection and
    a mapping function, would return a dictionary of the key items, which are
    associated with a list of matching items.
    """
    def group_into(collection: Sequence[S], dictionary: Dict[K, List[S]]) -> Dict[K, List[S]]:
        if len(collection) == 0:
            return dictionary

        head, *tail = collection
        dictionary[key(head)].append(head)

        return group_into(tail, dictionary)

    return group_into(data, defaultdict(list))


def group_by_imperative(key: Callable[[S], K], data: Iterable[K]) -> Dict[K, List[S]]:
    """
    This function is same as group_by_recursive, except that this function replaces
    recursion with an explicit loop, to remove any stack limits imposed by Python
    environment.
    """
    dictionary: Dict[K, List[S]] = defaultdict(list)
    for head in data:
        dictionary[key(head)].append(head)
    return dictionary
