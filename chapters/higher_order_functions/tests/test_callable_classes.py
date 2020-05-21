import pytest
import callable_classes as cc
from math import log as mlog
from typing import List

def compare_numeric_lists(list1: List[float], list2: List[float]) -> bool:
    eps = 0.0001
    for (v1, v2) in zip(list1, list2):
        if pytest.approx(v1, eps) != pytest.approx(v2, eps):
            return False
    return True


def test_nullaware() -> None:
    null_log_scale = cc.NullAware(mlog)
    scaled = map(null_log_scale, [10, 100, None, 50, 60])
    print(list(scaled))
    assert(compare_numeric_lists(list(scaled), [2.3025850929, 4.605170185988, None, 3.912023005428, 4.094344562]))


def test_count_not_none() -> None:
    assert(cc.count_not_none([1, 2, 3, None, 5, 6, None]) == 5)


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
