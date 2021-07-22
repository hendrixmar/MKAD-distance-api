import numpy as np
from shapely.geometry import Point

from region import MKAD_REGION, MKAD_CORDINATE
import os
from yandex_geocode_model import GeocodeYandexPoint



__api_key__ = os.environ.get('API_YANDEX_KEY', None)



def calculate_distance(address : str) -> float:

    address_point = GeocodeYandexPoint(__api_key__, address)


    if address_point.within(MKAD_REGION):
        return -1.0
    else:
        return address_point.haversine_distance(MKAD_CORDINATE)




