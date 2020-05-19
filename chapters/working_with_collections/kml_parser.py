"""
This module provides parsing of Keyhole Markup Language (KML) files that contain
geographic information encoded in a number of Placemark tags.
Below is an example:

<Placemark>
    <Point>
        <coordinates>-76.33029518659048,
                     37.54901619777347, 0</coordinates>
    </Point>
</Placemark>

Parsing an XML file can be approached at two levels of abstraction. At the
lower level, we need to locate the various tags, attribute values, and
content within the XML file. At a higher level, we want to make useful
objects out of the text and attribute values.
"""

import xml.etree.ElementTree as XML
from typing import Text, List, TextIO, Iterable, Tuple
from chapters.working_with_collections import haversine

def row_iter_kml(file_obj: TextIO) -> Iterable[List[Text]]:
    ns_map = {
        "ns0": "http://www.opengis.net/kml/2.2",
        "ns1": "http://www.google.com/kml/ext/2.2"
    }
    path_to_points = ("./ns0:Document/ns0:Folder/ns0:Placemark/ns0:Point/ns0:coordinates")
    doc = XML.parse(file_obj)

    return (comma_split(Text(coordinates.text)) for coordinates in doc.findall(path_to_points, ns_map))


def comma_split(text: Text) -> List[Text]:
    return text.split(",")


def pick_lat_lon(lon: Text, lat: Text, alt: Text) -> Tuple[Text, Text]:
    return lat,lon


Rows = Iterable[List[Text]]
LL_Text = Tuple[Text,Text]
LL_Text_Iter = Iterable[LL_Text]
LL_Float_Iter = Iterable[Tuple[float, float]]


def lat_lon_kml(row_iter: Rows) -> LL_Text_Iter:
    """
    This function will apply the pick_lat_lon() function to each row from a
    source iterator. We've used *row to assign each element of the row-three
    tuple to separate parameters of the pick_lat_lon() function. The function
    can then extract and reorder the two relevant values from each three-tuple
    """
    return (pick_lat_lon(*row) for row in row_iter)



def float_from_pair(lat_lon_iter: LL_Text_Iter) -> LL_Float_Iter:
    return (
        tuple((float(lat), float(lon)))
        for lat, lon in lat_lon_iter
    )


def legs(source: TextIO) -> LL_Float_Iter:
    iterator = float_from_pair(lat_lon_kml(row_iter_kml(source)))
    begin = next(iterator)
    for end in iterator:
        yield begin, end
        begin = end

    # return float_from_pair(lat_lon_kml(row_iter_kml(source)))



def trip(source: TextIO) -> Iterable[Tuple[haversine.Point, haversine.Point, float]]:
    return (
            tuple((start, end, round(haversine.haversine(start, end), 4)))
            for start, end in legs(source)
           )
