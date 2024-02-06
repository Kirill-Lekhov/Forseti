from forseti_lang.checkers.staples import check_staples
from forseti_lang.checkers.syntax import check_syntax


def check_all(condition: str):
	check_staples(condition)
	check_syntax(condition)
