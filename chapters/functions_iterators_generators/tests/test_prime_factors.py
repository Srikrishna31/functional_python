import pytest
from chapters.functions_iterators_generators import prime_factors as pf
from typing import List

TEST_VALUES = {
    8 : [2,2,2],
    31 : [31],
    101 : [101],
    9 : [3,3],
    12 : [2,2,3],
    6 : [2,3],
    24 : [2,2,2,3]
}


def get_prime_factors_list(n : int) -> List[int]:
    return [i for i in pf.pfactors(n)]


def get_prime_factors_recursive_list(n : int) -> List[int]:
    return [i for i in pf.pfactors_recursive(n)]


def test_prime_factors():
    for k,v in TEST_VALUES.items():
        assert get_prime_factors_list(k) == v


def test_prime_factors_recursive():
    for k, v in TEST_VALUES.items():
        assert get_prime_factors_recursive_list(k) == v


if __name__ == "__main__":
    SystemExit(pytest.main([__file__, "-v"]))
