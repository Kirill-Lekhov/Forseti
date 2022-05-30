from .base import BaseFunction
from ..exceptions import ForsetiFunctionSyntaxError

from re import search, split as re_split


class Nearby(BaseFunction):
	def __init__(self, command: str, text: str):
		self.arguments = []
		self.left_side_argument = ""
		super().__init__(command, text)

	def check_command(self):
		if "|nearby" not in self.command:
			raise ForsetiFunctionSyntaxError("Unsupported command syntax")

		command_parts = self.command.split(" |nearby ")

		if len(command_parts) != 2:
			raise ForsetiFunctionSyntaxError("Command doesn't support combined-condition")

		self.left_side_argument, self.arguments = command_parts
		self.arguments = self.arguments.split(" | ")

	def execute(self) -> bool:
		if not search(self.left_side_argument, self.text):
			return False

		text_parts = list(map(lambda x: x.strip(), re_split(self.left_side_argument, self.text)))
		parts_number = len(text_parts)

		for i in range(parts_number-1):
			left_side, right_side = "", ""

			if text_parts[i]:
				left_side = text_parts[i].split()[-1]

			if text_parts[i+1]:
				right_side = text_parts[i + 1].split()[0]

			if any(map(lambda x: search(x, left_side+right_side), self.arguments)):
				return True

		return False
