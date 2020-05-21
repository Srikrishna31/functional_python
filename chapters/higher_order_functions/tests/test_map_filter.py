import pytest
import map_filter as mf

def test_star_map() -> None:
    LIST = [1,2,3,4]
    assert(list(mf.star_map(lambda x : x**2, LIST)) == [1,4,9,16])


def test_star_filter() -> None:
    LIST = [1,2,3,4,5,6,7,8,9,10]
    assert(list(mf.star_filter(lambda x : x % 2 == 0, LIST)) == [(2,),(4,),(6,),(8,),(10,)])


def test_group_filter_iter() -> None:
    assert(list(mf.group_filter_iter(
        7,
        lambda x: x % 3 == 0 or x % 5 == 0,
        range(1,100)
    )) ==
    [(3, 5, 6, 9, 10, 12, 15),
     (18, 20, 21, 24, 25, 27, 30),
     (33, 35, 36, 39, 40, 42, 45),
     (48, 50, 51, 54, 55, 57, 60),
     (63, 65, 66, 69, 70, 72, 75),
     (78, 80, 81, 84, 85, 87, 90),
     (93, 95, 96, 99)])


def test_first() -> None:
    assert(mf.first(lambda x: x % 2 == 0, [1,3,5,7,8]) == 8)


def test_isprimeh() -> None:
    assert(mf.isprimeh(17) == True)


def test_map_not_none() -> None:
    assert(list(mf.map_not_none(
        int, ["1", "2", "abc", "3", "def", "4"]
    )) == [1,2,3,4])


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
