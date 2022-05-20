from .base import BaseFunction


class Length(BaseFunction):
	def __init__(self, command: str, text: str):
		super().__init__(command, text)

	def check_command(self):
		command_prefix = self.command[:3]

		if "|ll" == command_prefix or "|lg" == command_prefix:
			if not self.command[3:].isdigit():
				raise ValueError("After |ll or |lg construction must be number")

		else:
			raise SyntaxError("Unsupported command syntax")

	def execute(self) -> bool:
		if "|ll" in self.command:
			return len(self.text) < int(self.command[3:])

		if "|lg" in self.command:
			return len(self.text) > int(self.command[3:])
