from functools import reduce
from shapely.geometry import Point
from utility import LOG

from utility import sanatize
import urllib.request
import json
import numpy as np


class GeocodeYandexPoint(Point):

    def __init__(self, api_key: str,
                 address: str):

        try:
            address_sanitised = sanatize(address)
            http_response = urllib.request.urlopen(
                f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={address_sanitised}&lang=en-US&format"
                f"=json").read()
        except Exception as x:

            LOG.exception(f"Exception {x}")

        json_data = json.loads(http_response)
        # A list of all the keys I have to traverse to get the coordinate point in the json file
        # so I can traverse the keys directly using the reduce function
        key_path = ["response", "GeoObjectCollection", "featureMember", 0, "GeoObject", "Point", "pos"]
        point_string = reduce(lambda p, c: p[c], key_path, json_data)
        coordinate_tuple = tuple(float(i) for i in point_string.split())

        # Instance the super class using the tuple of floats
        super().__init__(coordinate_tuple)

    def haversine_distance(self, coordinate: Point) -> float:
        """
              Obtain the haversine distance between two cordinates points in the map

                  :return: haversine distance in km:
                  :rtype: float
        """
        lat1, lon1 = self.y, self.x
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

        # Return the result mulitplied by world radius
        return rad * c
