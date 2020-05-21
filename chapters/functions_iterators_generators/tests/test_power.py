import pytest
import power

def test_power_shifty():
    assert power.shift(4) == 15
    assert power.shift(8) == 255


def test_power_multy():
    assert power.mult(4) == 15
    assert power.mult(8) == 255


def test_power_faster():
    assert power.fast(4) == 15
    assert power.fast(8) == 255


if __name__=="__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
