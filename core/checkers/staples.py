def check_staples(command: str) -> None:
	assert command.count('(') == command.count(')'), "No closing/opening brackets"
