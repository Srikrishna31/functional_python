from typing import Iterator
import math
from symbol import yield_expr


def pfactors(x: int) -> Iterator[int] :
    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactors(x // 2)
        return

    for i in range(3, int(math.sqrt(x) + .5) + 1, 2):
        if x % i == 0:
            yield i
            if x // i > 1:
                yield from pfactors(x // i)
                return
    yield x


def pfactors_recursive(x: int) -> Iterator[int] :
    def go(x : int, n : int) -> Iterator[int]:
        if n * n > x:
            yield x
            return
        if x % n == 0:
            yield n
            if x // n > 1:
                yield from go(x // n, n)
        else:
            yield from go(x, n + 2)

    if x % 2 == 0:
        yield 2
        if x // 2 > 1:
            yield from pfactors_recursive(x // 2)
        return

    yield from go(x, 3)



