from typing import Set


AND = "AND"
OR = "OR"
NOT = "NOT"
OPEN_PARENTHESIS = "("
CLOSE_PARENTHESIS = ")"

# GROUPS
BINARY_OPERATORS: Set[str] = {AND, OR}
UNARY_OPERATORS: Set[str] = {NOT}
OPERATORS: Set[str] = BINARY_OPERATORS | UNARY_OPERATORS
PARENTHESES: Set[str] = {OPEN_PARENTHESIS, CLOSE_PARENTHESIS}
