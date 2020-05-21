import sequence_structure as ss
import pytest

LIST1 = [1,2,3,4,5,6]
LIST2 = [1,2,3,4,5,6,7]

def test_group_by_seq():
    assert ss.group_by_seq(2, LIST1) == [(1,2), (3,4), (5,6)]
    assert ss.group_by_seq(2, LIST2) == [(1,2), (3,4), (5,6), (7,)]



def test_group_by_iter():
    assert list(ss.group_by_iter(2, iter(LIST1))) == [(1,2), (3,4), (5,6)]
    assert list(ss.group_by_iter(2, iter(LIST2))) == [(1,2), (3,4), (5,6), (7,)]


def test_group_by_seq_alternative():
    assert list(ss.group_by_seq_alternative(2, LIST1)) == [(1,2), (3,4), (5,6)]
    assert list(ss.group_by_seq_alternative(2, LIST2)) == [(1,2), (3,4), (5,6),]


def test_digits():
    assert(list(ss.digits(16, 2)) == [0,0,0,0,1])
    assert(list(ss.digits(7, 8)) == [7])


def test_digits_reversed():
    assert(list(ss.reversed_digits(16, 2)) == [1,0,0,0,0])
    assert(list(ss.reversed_digits(7,8)) == [7])


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-rPx", "-v"]))
