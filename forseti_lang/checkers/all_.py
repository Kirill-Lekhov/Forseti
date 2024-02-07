from forseti_lang.checkers.parenthesis import check_parentheses
from forseti_lang.checkers.syntax import check_syntax


def check_all(condition: str):
	check_parentheses(condition)
	check_syntax(condition)
