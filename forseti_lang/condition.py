def replace_ru_statements(condition: str) -> str:
	return (
		condition
		.replace(" И ", " AND ")
		.replace(" ИЛИ ", " OR ")
		.replace("НЕ ", "NOT ")
	)
