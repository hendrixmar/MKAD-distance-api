import numpy as np
from shapely.geometry import Point


def haversine_distance(coordinate: Point) -> float:
    """
          Obtain the haversine distance between two cordinates points in the map

            :param coordinate: shapely.geometry.point
            :return: haversine distance in km:

    """
    # MKAD coordinate
    lat1, lon1 = 55.755826, 37.6173

    # address  coordinate
    lat2, lon2 = coordinate.y, coordinate.x
    # distance between latitudes
    # and longitudes
    distance_lat = np.radians(lat2 - lat1)
    distance_lon = np.radians(lon2 - lon1)

    # convert to radians
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)

    # apply the haversine formula
    a = (pow(np.sin(distance_lat / 2), 2)
         + pow(np.sin(distance_lon / 2), 2)
         * np.cos(lat1) * np.cos(lat2))
    rad = 6371
    c = 2 * np.arcsin(np.sqrt(a))

    # Return the result multiplied by world radius
    return rad * c




def test_answer():
    assert 3 == 3




