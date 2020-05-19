import bisect
from collections import Mapping
from typing import Iterable, Tuple, Any


"""
This class uses a binary tree to store the keys, so that a large amount
of memory needn't be allocated upfront. Other than that, this class is
exactly same as the built in dict class.
"""


class StaticMapping(Mapping):
    def __init__(self, iterable: Iterable[Tuple[Any, Any]]) -> None:
        self._data = tuple(iterable)
        self._keys = tuple(sorted(key for key, _ in self._data))


    def __getitem__(self, key):
        ix = bisect.bisect_left(self._keys, key)
        if ix != len(self._keys) and self._keys[ix] == key:
            return self._data[ix][1]
        raise ValueError(f"{key} not found")


    def __iter__(self):
        return iter(self.keys)


    def __len__(self):
        return len(self.keys)
