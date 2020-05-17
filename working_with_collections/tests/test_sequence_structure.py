from working_with_collections import sequence_structure as ss
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


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-rPx", "-v"]))