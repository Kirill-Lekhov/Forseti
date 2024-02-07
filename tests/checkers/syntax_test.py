from forseti_lang.exceptions import ForsetiSyntaxError
from forseti_lang.checkers.syntax import check_syntax

import pytest


@pytest.mark.parametrize(
	"condition",
	[
		"AND SomeCommand",
		"SomeCommand AND",
		"OR SomeCommand",
		"SomeCommand OR",
		"И SomeCommand",
		"SomeCommand И",
		"ИЛИ SomeCommand",
		"SomeCommand ИЛИ",
		"NOT SomeCommand",
		"SomeCommand NOT",
	]
)
def test_check_syntax_errors(condition):
	with pytest.raises(ForsetiSyntaxError):
		check_syntax(condition)


@pytest.mark.parametrize(
	"condition",
	[
		"SomeCommand OR SomeCondition (Wrong condition)",
		"(Wrong condition) SomeCommand OR SomeCondition",
		"SomeCommand (Wrong condition) SomeCondition",
	]
)
def test_check_syntax_errors(condition):
	with pytest.raises(ForsetiSyntaxError, match="You can't use parentheses without operators"):
		check_syntax(condition)


@pytest.mark.parametrize(
	"condition",
	[
		"SomeCommand1 OR NOT SomeCommand2",
		"SomeCommand1 NOT NOT SomeCommand2",
		"SomeCommand1 NOT SomeCommand2",
	]
)
def test_check_parentheses_errors(condition):
	with pytest.raises(ForsetiSyntaxError, match="Operator 'NOT' cannot be used without operator 'AND'"):
		check_syntax(condition)
