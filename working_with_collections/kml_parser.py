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

def lat_lon_kml(row_iter: Rows) -> Iterable[LL_Text]:
    """
    This function will apply the pick_lat_lon() function to each row from a
    source iterator. We've used *row to assign each element of the row-three
    tuple to separate parameters of the pick_lat_lon() function. The function
    can then extract and reorder the two relevant values from each three-tuple
    """
    return (pick_lat_lon(*row) for row in row_iter)

