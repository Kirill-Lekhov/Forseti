def check_staples(command: str) -> None:
	assert command.count('(') == command.count(')'), "Нет закрывающей/открывающей скобки"
