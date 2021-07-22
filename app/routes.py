from flask import Blueprint
from utility import LOG
import os
from logic import calculate_distance


bp = Blueprint('example_blueprint', __name__)

@bp.route('/distance/<address>')
def index(address: str):

    # .info('Mostrando los posts del blog')
    LOG.info("Call health ok "+address)
    result = calculate_distance(address)

    return address
