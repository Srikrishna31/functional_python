import adjacent_pairer as ap
import pytest

def test_pairs_recursive() -> None:
    l = list(t for t in ap.pairs_recursive((i for i in range (1, 4))))
    print(l)
    assert(l == [(1,2), (2,3)])



def test_pairs() -> None:
    l = list(t for t in ap.pairs((i for i in range(1, 4))))
    print(l)
    assert(l == [(1,2), (2,3)])


def test_pairs_empty() -> None:
    l = list(t for t in ap.pairs((i for i in range(1))))
    print(l)
    assert( l == [])



if __name__ == "__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
