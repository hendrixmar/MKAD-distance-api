from flask import Blueprint
from utility import LOG
import os
from logic import calculate_distance


bp = Blueprint('example_blueprint', __name__)

@bp.route('/distance/<address>')
def index(address: str):

    # .info('Mostrando los posts del blog')
    LOG.info("Call health ok {}")
    result = calculate_distance(address)

    if 0 < result:
        return f"Distance from {address} to MKAD: {result}KM"
    else:
        return f"{address} is inside of MKAD"