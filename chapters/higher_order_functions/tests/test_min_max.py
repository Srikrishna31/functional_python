import min_max
import pytest

def test_long():
    with open("chapters/working_with_collections/data/KML_Sample.kml", "r") as f:
        print(min_max.long(f))
    assert(True)


def test_short():
    with open("chapters/working_with_collections/data/KML_Sample.kml", "r") as f:
        print(min_max.short(f))
    assert(True)


def test_max_like():
    with open("chapters/working_with_collections/data/KML_Sample.kml", "r") as f:
        print(min_max.max_like(f))
    assert(True)


def test_min_like():
    with open("chapters/working_with_collections/data/KML_Sample.kml", "r") as f:
        print(min_max.min_like(f))
    assert(True)


if __name__=="__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
