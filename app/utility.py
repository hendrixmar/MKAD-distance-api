import re
import logging


logging.basicConfig(handlers=[logging.FileHandler('example.log', 'r+', 'utf-8')])
LOG = logging.getLogger(__name__)

def sanatize(input_string : str) -> str:

    input_string = re.sub("[<|>|*|%|&|:|?|\ ]", "+", input_string)

    return input_string


