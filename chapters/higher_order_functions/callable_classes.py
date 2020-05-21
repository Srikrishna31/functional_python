from typing import Callable, Optional, Any, Iterable

"""
This module presents a couple of examples, defining higher-order functions as
callable classes. This builds on the idea of writing generator functions.
This allows us to use statement features of Python, and also apply static
configuration when creating the higher-order functions.
"""

class NullAware:
    """
    This class is used to create a new function that is nullaware. When an
    instance of this class is created, a function, some_func is provided. The
    only restriction is that some_func be Callable[[Any], Any]. This means the
    argument takes a single argument and results in a single result.
    The implementation of the __call__() method handles the use of None objects
    as an argument. This method has the effect of making the resulting object
    Callable[[Optional[Any]], Optional[Any]]
    """
    def __init__(self, some_func: Callable[[Any], Any]) -> None:
        self.some_func = some_func

    def __call__(self, arg: Optional[Any]) -> Optional[Any]:
        return None if arg is None else self.some_func(arg)


class Map_Filter:
    """
    This class has precisely two slots in each object; this puts a few constraints
    on our ability to use the function as a stateful object. It doesn't prevent all
    modifications to the resulting object, but it limits us to jsut two attributes.
    Attempting to add attributes results in an exception.
    The initialization method, __init__(), stows the two function names, filter and
    func, in the object's instance variables. The __call__() method returns a value
    based on a generator expression that uses the two internal function definitions.
    The self.filter() is used to pass or reject items. The self.function() is used
    to transform objects that are passed by the filter() function.
    """
    __slots__ = ["filter", "function"]
    def __init__(self, filt: Callable[[Any], bool], func: Callable[[Any], float]) -> None:
        self.filter = filt
        self.function = func

    def __call__(self, iterable: Iterable) -> float:
        return sum(self.function(x) for x in iterable if self.filter(x))


count_not_none = Map_Filter(
    lambda x : x is not None,
    lambda _ : 1
)
