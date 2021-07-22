import numpy as np
from shapely.geometry import Point

from region import MKAD_REGION, MKAD_CORDINATE
import os
from yandex_geocode_model import GeocodeYandexPoint



API_KEY = os.environ.get('API_YANDEX_KEY', None)




def calculate_distance(address : str) -> float:

    address_point = GeocodeYandexPoint(API_KEY, address)


    if address_point.within(MKAD_REGION):
        return address_point.haversine_distance(MKAD_CORDINATE)
    else:
        return -1.0




