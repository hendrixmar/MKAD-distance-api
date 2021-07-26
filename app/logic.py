import os
from functools import reduce
import numpy as np
import requests
from shapely.geometry import Point
from utility import sanitize_string, MKAD_REGION, flask_logger
from yandex_geocode_model import GeocodeYandexPoint

__api_key__ = os.environ.get('API_YANDEX_KEY_2', None)

def calculate_distance(address: str) -> {}:
    """
        Connect the different components of the logic of the API

            :param address:
            :return: metadata of the address
    """
    json_request = yandex_geocode_api(address)

    if "status" in json_request:
        return json_request

    address_point = GeocodeYandexPoint(json_request)

    if address_point.within(MKAD_REGION):
        return {"status": "address is located inside MKAD"}
    else:
        return {"distance" : haversine_distance(address_point) }

def yandex_geocode_api(address: str) -> {}:
    """
        Gets the metadata if the input address by doing a http request to yandex geocode api

            :param address:
            :return: metadata of the address
    """
    address_sanitised = sanitize_string(address)

    try:
        http_response = requests.get(
            f"https://geocode-maps.yandex.ru/1.x/"
            f"?apikey={__api_key__}&"
            f"geocode={address_sanitised}&"
            f"lang=en-US&"
            f"format=json")
    except:
        flask_logger.exception("HTTP call exception")

    if http_response.status_code == 200:
        json_data = http_response.json()

        # Search for the key found to know how many result we got
        # if the number is equal to 0 it returns an empty dictionary
        key_path = ["response", "GeoObjectCollection", "metaDataProperty", "GeocoderResponseMetaData", "found"]
        result = reduce(lambda p, c: p[c], key_path, json_data)

        return {"status": "error", "response" : "No metadata found"} if result == "0" else json_data

    else:
        return {"status": "error",  "response" : f"HTTP error {http_response.status_code} from yandex API"}

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
