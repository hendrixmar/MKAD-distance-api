from functools import reduce
from shapely.geometry import Point


class GeocodeYandexPoint(Point):

    def __init__(self, metadata: {}):
        # A list of all the keys I have to traverse to get the coordinate point in the json file
        # so I can traverse the keys directly using the reduce function
        key_path = ["response", "GeoObjectCollection", "featureMember", 0, "GeoObject", "Point", "pos"]
        point_string = reduce(lambda p, c: p[c], key_path, metadata)
        coordinate_tuple = tuple(float(i) for i in point_string.split())

        # Instance the super class using the tuple of floats
        super().__init__(coordinate_tuple)
