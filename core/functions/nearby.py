from .base import BaseFunction

from re import search, split as re_split


class Nearby(BaseFunction):
	def __init__(self, command: str, text: str):
		self.arguments = []
		self.left_side_argument = ""
		super().__init__(command, text)

	def check_command(self):
		if "|nearby" not in self.command:
			raise SyntaxError("Unsupported command syntax")

		command_parts = self.command.split(" |nearby ")

		if len(command_parts) != 2:
			raise SyntaxError("Unsupported command syntax")

		self.left_side_argument, self.arguments = command_parts
		self.arguments = self.arguments.split(" | ")

	def execute(self) -> bool:
		for part in re_split(self.left_side_argument, self.text):
			if not part:
				continue

			nearby_word = part.split()[0]

			if any(map(lambda x: search(x, nearby_word), self.arguments)):
				return True

		return False


if __name__ == "__main__":
	df = Nearby("some |nearby body | once | told | me", "... some body ...").res
	print(df)

	df = Nearby("some |nearby body | on | me", "... some once ...").res
	print(df)

	df = Nearby("some |nearby to[l]?[d]?", "... some told ...").res
	print(df)

	df = Nearby("some |nearby body | once | told | me", "... some world told ...").res
	print(df)
