import pytest
import reductions

TEST = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
EXPECTED = {0: [("b", 2), ("d", 4)],
            1: [("a", 1), ("c", 3), ("e", 5)]}

key = lambda x: x[1]%2

def test_group_by_recursive() -> None:
    assert (reductions.group_by_recursive(key, TEST) == EXPECTED)


def test_group_by_imperative() -> None:
    assert (reductions.group_by_imperative(key, TEST) == EXPECTED)


def test_group_by() -> None:
    assert(reductions.group_by_recursive(key,TEST) == reductions.group_by_imperative(key, TEST))


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-s", "-vv"]))
