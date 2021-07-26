from flask import Blueprint
from utility import flask_logger
from logic import calculate_distance

bp = Blueprint('example_blueprint', __name__)

@bp.route('/distance/<address>')
def index(address: str):

    result = calculate_distance(address)

    if "distance" in result:
        flask_logger.info(f"Distance: {result['Distance']}")
        return {"message": f"Distance from {address} to MKAD: {result}KM",  "distance" : result["Distance"] }
    else:
        flask_logger.info(result["response"])
        return result



