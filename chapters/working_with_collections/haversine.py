"""
This module provides a simplistic implementation of haversine function which is
copied from the web.
"""
from math import radians, sin, cos, sqrt, asin
from typing import Tuple

MI = 3959
NM = 3440
KM = 6371
Point = Tuple[float, float]

def haversine(p1: Point, p2: Point, R: float=NM) -> float:
    """
    This functions calculates distance in kilometers between a pair of
    latitudes and longitudes.
    """
    lat_1, lon_1 = p1
    lat_2, lon_2 = p2
    d_lat = radians(lat_2 - lat_1)
    d_lon = radians(lon_2 - lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    a = sqrt(sin(d_lat / 2) ** 2 + cos(lat_1) * cos(lat_2) * sin(d_lon / 2) ** 2)
    c = 2 * asin(a)

    return R * c