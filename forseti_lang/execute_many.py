from forseti_lang.preparing import prepare_condition
from forseti_lang.execute import execute_condition_parts

from typing import Iterable, Generator, Tuple
from copy import deepcopy


def execute_many(conditions: Iterable[str], text: str, check: bool = True) -> Generator[str, None, None]:
	for condition in conditions:
		condition_parts = prepare_condition(condition, check)

		if execute_condition_parts(condition_parts, text):
			yield condition


def execute_many_to_many(
	conditions: Iterable[str],
	texts: Iterable[str],
	check: bool = True,
) -> Generator[Tuple[str, str], None, None]:
	parts_of_conditions = {}

	for condition in conditions:
		parts_of_conditions[condition] = prepare_condition(condition, check)

	for condition, parts in parts_of_conditions.items():
		for text in texts:
			if execute_condition_parts(deepcopy(parts), text):
				yield text, condition
