from forseti_lang.parse import parse_items
from forseti_lang.checkers.all_ import check_all
from forseti_lang.condition import replace_ru_statements

from typing import List


def prepare_condition(condition: str, check: bool = True) -> List[List[str]]:
	if check:
		check_all(condition)

	condition = replace_ru_statements(condition)
	return parse_items(condition)
