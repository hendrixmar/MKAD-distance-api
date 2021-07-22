import re
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
LOG = logging.getLogger(__name__)

def sanatize(input_string : str) -> str:

    input_string = re.sub("[<|>|*|%|&|:|?|\ ]", "+", input_string)

    return input_string


