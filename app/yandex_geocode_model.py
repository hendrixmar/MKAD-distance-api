from functools import reduce
from shapely.geometry import Point
from utility import sanatize, LOG
import urllib.request
import json
import numpy as np


class GeocodeYandexPoint(Point):

    def __init__(self, api_key: str,
                 address: str):

        try:
            address_sanitised = sanatize(address)
            http_response = urllib.request.urlopen(
                f"https://geocode-maps.yandex.ru/1.x/?apikey={api_key}&geocode={address_sanitised}&lang=en-US&format=json&skip=").read()

        except Exception as x:
            LOG.exception(x)

        json_data = json.loads(http_response)

        # A list of all the keys I have to traverse to get the cordinate point in the json file
        # so I can traverse the keys directly using the reduce function
        key_path = ["response", "GeoObjectCollection", "featureMember", 0, "GeoObject", "Point", "pos"]
        point_string = reduce(lambda p, c: p[c], key_path, json_data)
        cordinate_tupple = tuple(float(i) for i in point_string.split())

        # Instance the super class using the tuple of floats
        super().__init__(cordinate_tupple)

    def haversine_distance(self, coordinate: Point) -> float:
        """
        Obtain the haversine distance between two cordinates points in the map

            :return: haversine distance in km:
            :rtype: float
        """

        # radio of the world expressed in KM
        RADIUS = 6371

        # convert the latitude of the two points in radianst
        PHI1 = np.radians(self.x)
        PHI2 = np.radians(coordinate.x)

        #
        DELTA_PHI = np.radians(coordinate.x - self.x)
        DELTA_LAMBDA = np.radians(coordinate.y - self.y)

        a = np.sin(DELTA_PHI / 2) ** 2 + np.cos(PHI1) * np.cos(PHI2) * np.sin(DELTA_LAMBDA / 2) ** 2
        result = RADIUS * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))

        return np.round(result, 2)
