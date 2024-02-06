from forseti_lang.parse import parse_items
from forseti_lang.checkers.all_ import check_all

from typing import List


def prepare_condition(condition: str, check: bool = True) -> List[List[str]]:
	if check:
		check_all(condition)

	condition = (
		condition
		.replace(" И ", " AND ")
		.replace(" ИЛИ ", " OR ")
		.replace("НЕ ", "NOT ")
	)
	return parse_items(condition)
