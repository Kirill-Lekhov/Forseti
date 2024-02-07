from forseti_lang.functions.distance import Distance
from forseti_lang.functions.length import Length
from forseti_lang.functions.nearby import Nearby
from forseti_lang.functions.regex import Regex
from forseti_lang.operator import TRUE, FALSE

from re import search


def execute_automatically(command: str, text: str) -> bool:
	if command == TRUE:
		return True

	elif command == FALSE:
		return False

	elif "|l" in command:
		return Length(command, text).res

	elif search(Distance.COMMAND_FORMAT, command):
		return Distance(command, text).res

	elif "|nearby " in command:
		return Nearby(command, text).res

	else:
		return Regex(command, text).res
