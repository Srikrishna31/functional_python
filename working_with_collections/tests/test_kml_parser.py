from working_with_collections import kml_parser
import pytest
#According to the following stack overflow post, import urllib.request rather than just urllib.
# https://stackoverflow.com/questions/37042152/python-3-5-1-urllib-has-no-attribute-request
import urllib.request

def test_kml_parser():
    with open("working_with_collections/data/KML_Sample.kml", "r") as source:
        for  row in kml_parser.row_iter_kml(source):
            print (row)

    assert True


def test_lat_lon():
    url = "https://developers.google.com/kml/documentation/KML_Samples.kml"

    with urllib.request.urlopen(url) as source:
        v1 = tuple(kml_parser.lat_lon_kml(kml_parser.row_iter_kml(source)))
    print(v1)

    assert True


if __name__ == "__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
