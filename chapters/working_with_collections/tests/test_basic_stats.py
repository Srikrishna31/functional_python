from chapters.working_with_collections import basic_stats as bs
import pytest


def test_correlation():
    xi = [ 1.47, 1.50, 1.52, 1.55, 1.57, 1.60, 1.63, 1.65,
           1.68, 1.70, 1.73, 1.75, 1.78, 1.80, 1.83, ]  # Height (m)
    yi = [ 52.21, 53.12, 54.48, 55.84, 57.20, 58.57, 59.93, 61.29,
           63.11, 64.47, 66.28, 68.10, 69.92, 72.19, 74.46, ]  # Mass (kg)

    assert round(bs.corr(xi, yi), 5) == pytest.approx(0.99458, 0.001)


def test_std_value():
    d = [2,4,4,4,5,5,7,9]
    m = bs.mean(d)
    s = bs.std_dev(d)
    assert list(bs.std_value(x, m, s) for x in d) == [-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-v", "-rPfEs"]))
