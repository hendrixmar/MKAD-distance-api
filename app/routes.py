from flask import Blueprint
from utility import flask_logger
from logic import calculate_distance

bp = Blueprint('example_blueprint', __name__)


@bp.route('/distance/<address>')
def index(address: str):
	result = calculate_distance(address)

	if "distance" in result:
		flask_logger.info(f"Distance: {result['distance']}")
		return {"message": f'Distance from {address} to MKAD: {result["distance"]}KM', "distance": result["distance"]}
	else:
		flask_logger.info(result["response"])
		return result
