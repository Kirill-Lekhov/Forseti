from typing import List


def parse_items(condition: str) -> List[List[str]]:
	buffer = ""
	stack = [[]]
	conditions = list()
	conditions.append(stack[-1])

	for char in condition:
		if char == "(":
			if buffer:
				stack[-1].append(buffer[:])

			stack.append([])
			stack[-2].append(f"ATOM_{len(conditions)}")
			conditions.append(stack[-1])

			buffer = ""

		elif char == ")":
			if not stack:
				raise SyntaxError("Закрывающая скобка встречена перед использованием открывающей")

			if buffer:
				stack[-1].append(buffer[:])

			del stack[-1]

			buffer = ""

		else:
			buffer += char

	if buffer:
		conditions[0].append(buffer)

	return conditions


if __name__ == "__main__":
	print(parse_items("(True AND False) AND ((True AND False) OR False) AND False"))
