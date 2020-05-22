import pytest
import recursions

def test_factorial_recursive():
    assert(recursions.factorial_recursive(5) == 120)

if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
