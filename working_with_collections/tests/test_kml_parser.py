from working_with_collections import kml_parser
import pytest


def test_kml_parser():
    with open("working_with_collections/data/KML_Sample.kml", "r") as source:
        for  row in kml_parser.row_iter_kml(source):
            print (row)

    assert True


if __name__ == "__main__":
    SystemExit(pytest.main([__file__, "-v", "-s"]))
