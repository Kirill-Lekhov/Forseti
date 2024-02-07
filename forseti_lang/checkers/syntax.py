from forseti_lang.exceptions import ForsetiSyntaxError
from forseti_lang.condition import replace_ru_statements
from forseti_lang.operator import OPERATORS, AND, NOT, OR, OPEN_PARENTHESIS, CLOSE_PARENTHESIS, BINARY_OPERATORS

from typing import List, Tuple, Optional

ERRORS = {
	"operator_position": "Operator '{}' is used without expression '{}'",
}


def check_syntax(command: str) -> None:
	parts = replace_ru_statements(command).split()
	parts_count = len(parts)

	if not parts:
		return

	if parts[0] in OPERATORS:
		raise ForsetiSyntaxError(ERRORS['operator_position'].format(parts[0], 'left-side'))

	if parts[-1] in OPERATORS:
		raise ForsetiSyntaxError(ERRORS['operator_position'].format(parts[-1], 'right-side'))

	for i in range(parts_count):
		part = parts[i]
		left_neighbor = parts[i-1] if i else None
		right_neighbor = parts[i+1] if i < parts_count - 1 else None

		if part in OPERATORS:
			check_operator(part, (left_neighbor, right_neighbor))
		else:
			check_parenthesis(part, (left_neighbor, right_neighbor))


def check_operator(operator: str, adjacent_parts: Tuple[Optional[str], Optional[str]]) -> None:
	if operator == NOT:
		if adjacent_parts[0] != AND:
			raise ForsetiSyntaxError("Operator 'NOT' cannot be used without operator 'AND'")

	if operator in BINARY_OPERATORS:
		if adjacent_parts[0] in BINARY_OPERATORS or adjacent_parts[1] in BINARY_OPERATORS:
			raise ForsetiSyntaxError(f"Binary operator {operator} cannot be used together with binary operator")

	else:
		raise NotImplementedError(f"Check of the '{operator}' operator is not implemented")


def check_parenthesis(parenthesis: str, adjacent_parts: Tuple[Optional[str], Optional[str]]) -> None:
	if adjacent_parts[0]:
		if adjacent_parts[0].rstrip()[-1] == CLOSE_PARENTHESIS and parenthesis not in OPERATORS:
			raise ForsetiSyntaxError("You can't use staples without operators")

	if adjacent_parts[1]:
		if adjacent_parts[1].lstrip()[0] == OPEN_PARENTHESIS and parenthesis not in OPERATORS:
			raise ForsetiSyntaxError("You can't use staples without operators")
