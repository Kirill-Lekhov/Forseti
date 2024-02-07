from forseti_lang.exceptions import ForsetiSyntaxError
from forseti_lang.checkers.parenthesis import check_parentheses

import pytest


@pytest.mark.parametrize(
	"condition",
	[
		"((True)",
		"(True))",
	]
)
def test_check_parentheses_errors(condition):
	with pytest.raises(ForsetiSyntaxError):
		check_parentheses(condition)


@pytest.mark.parametrize(
	"condition",
	[
		"(True)",
		"((True))",
		"True",
		"(True OR False) AND (False AND True)",
	]
)
def test_check_parentheses_results(condition):
	assert check_parentheses(condition) is None
