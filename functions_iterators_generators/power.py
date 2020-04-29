from typing import Callable


class Mersenne:
    def __init__(self, algorithm: Callable[[int], int]) -> None:
        self.pow2 = algorithm


    def __call__(self, arg: int) -> int:
        return self.pow2(arg) - 1


def shifty(b: int) -> int:
    return 1 << b


def multy(b: int) -> int:
    if b == 0: return 1
    return 2*multy(b - 1)


def faster(b: int) -> int:
    if b == 0: return 1
    if b % 2 == 1: return 2*faster(b - 1)
    t = faster(b // 2)
    return t * t


shift = Mersenne(shifty)
mult = Mersenne(multy)
fast = Mersenne(faster)