from chapters.working_with_collections import kml_parser
import pytest
#According to the following stack overflow post, import urllib.request rather than just urllib.
# https://stackoverflow.com/questions/37042152/python-3-5-1-urllib-has-no-attribute-request
import urllib.request

URL = "https://developers.google.com/kml/documentation/KML_Samples.kml"

def test_kml_parser() -> None:
    with open("working_with_collections/data/KML_Sample.kml", "r") as source:
        for  row in kml_parser.row_iter_kml(source):
            print (row)

    assert True


def test_lat_lon() -> None:
    with urllib.request.urlopen(URL) as source:
        for lat,lon in kml_parser.lat_lon_kml(kml_parser.row_iter_kml(source)):
            print((lat,lon))

    assert True


def test_float_pair() -> None:
    with urllib.request.urlopen(URL) as source:
        for start, end in kml_parser.legs(source):
            print((start, end))


    assert(True)


def test_trip() -> None:
    with urllib.request.urlopen(URL) as source:
        for start, end, dist in kml_parser.trip(source):
            print((start, end, dist))

    assert(True)



if __name__ == "__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
