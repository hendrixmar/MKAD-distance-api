from flask import Blueprint
from utility import flask_logger, sanatize_string
from logic import calculate_distance
import urllib.request

bp = Blueprint('example_blueprint', __name__)

@bp.route('/distance/<address>')
def index(address: str):

    # .info('Mostrando los posts del blog')
    flask_logger.info("Call health ok {}")
    result = calculate_distance(address)

    if 0 < result:
        flask_logger.info(f"{result}")
        return {"message": f"Distance from {address} to MKAD: {result}KM",  "distance" : result }
    elif result == -2.0:
        flask_logger.info(f"{result}")
        return {"message": f"{address} doesnt exist in the database",  "distance" : result }
    else:
        flask_logger.info(f"{result}")
        return {"message": f"{address} is inside of MKAD",  "distance" : result }


