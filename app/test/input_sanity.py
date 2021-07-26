import string
import random
import re
import pytest


def sanitize_string(input_string: str) -> str:
	return re.sub('[\\\!"\#\$%\&\'()\*,-./\:;<=>\?\@\[\]^^_`\{\|\}~+¡\ ]+', "+", input_string)


def test_answer():
	counter = 1

	letters = "".join(
		[string.ascii_uppercase, string.ascii_lowercase, string.ascii_letters, string.punctuation, string.digits])
	for _ in range(200):
		# printing lowercase
		letters = string.ascii_lowercase

		test_case = ''.join(random.choice(letters) for i in range(50))

		result = sanitize_string(test_case)

		if not re.match("[a-zA-Z0-9]+", result):
			pytest.fail(f"Test case {counter}: {result}")

		counter += 1
