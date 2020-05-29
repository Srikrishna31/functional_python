import pytest
import recursions


def test_factorial_recursive() -> None:
    assert(recursions.factorial_recursive(5) == 120)


def test_factorial_imperative() -> None:
    assert(recursions.factorial_imperative(6) == 720)


def test_factorial() -> None:
    for i in range(1, 50):
        assert(recursions.factorial_recursive(i) == recursions.factorial_imperative(i))


FIB_SERIES = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def test_fib_recursive() -> None:
    for i, v in enumerate(FIB_SERIES):
        assert(recursions.fib_recursive(i) == v)


def test_fib_imperative() -> None:
    for i, v in enumerate(FIB_SERIES):
        assert(recursions.fib_imperative(i) == v)


def test_fib() -> None:
    for i in range(1, 25):
        assert(recursions.fib_recursive(i) == recursions.fib_imperative(i))


def test_map_recursive() -> None:
    assert(recursions.map_recursive(lambda x:2**x, [0,1,2,3,4]) == [1,2,4,8,16])


def test_map_imperative() -> None:
    assert(list(recursions.map_imperative(lambda x:2**x, iter([0,1,2,3,4]))) == [1,2,4,8,16])


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
