from forseti_lang.exceptions import ForsetiSyntaxError
from forseti_lang.types import ConditionParts


def parse_items(condition: str) -> ConditionParts:
	buffer = ""
	stack = [[]]
	conditions = [stack[-1]]

	for char in condition:
		if char == "(":
			if not stack:
				raise ForsetiSyntaxError("The closing bracket is met before using the opening one")

			if buffer:
				stack[-1].append(buffer[:])

			stack.append([])
			stack[-2].append(len(conditions))
			conditions.append(stack[-1])

			buffer = ""

		elif char == ")":
			if not stack:
				raise ForsetiSyntaxError("The closing bracket is met before using the opening one")

			if buffer:
				stack[-1].append(buffer[:])

			del stack[-1]

			buffer = ""

		else:
			buffer += char

	if buffer:
		conditions[0].append(buffer)

	return conditions
