from forseti_lang.exceptions import ForsetiSyntaxError
from forseti_lang.operator import OPEN_PARENTHESIS, CLOSE_PARENTHESIS


def check_staples(command: str) -> None:
	if command.count(OPEN_PARENTHESIS) != command.count(CLOSE_PARENTHESIS):
		raise ForsetiSyntaxError("No closing/opening brackets")
