from forseti_lang.execute_many import execute_many, execute_many_to_many

from typing import Iterable, List, Tuple

import pytest


@pytest.mark.parametrize(
	"conditions, text, expected_result",
	[
		([], "", []),
		(['test'], "", []),
		(['test'], "empty string", []),
		(['test', 'test AND ost', 'test OR ost'], 'test', ['test', 'test OR ost']),
	],
)
def test_execute_many(conditions: Iterable[str], text: str, expected_result: List[str]):
	assert list(execute_many(conditions, text, False)) == expected_result


@pytest.mark.parametrize(
	"conditions, texts, expected_results",
	[
		([], [], []),
		([], ["text", "text"], []),
		(["FALSE AND (TRUE OR FALSE)"], [], []),
		(
			["(FALSE AND (TRUE OR FALSE)) OR TRUE", "text", "text AND NOT text"],
			["text", "text1", "test"],
			[
				("text", "(FALSE AND (TRUE OR FALSE)) OR TRUE"),
				("text1", "(FALSE AND (TRUE OR FALSE)) OR TRUE"),
				("test", "(FALSE AND (TRUE OR FALSE)) OR TRUE"),
				("text", "text"),
				("text1", "text"),
			],
		),
	],
)
def test_execute_many_to_many(conditions: Iterable[str], texts: Iterable[str], expected_results: List[Tuple[str, str]]):
	assert list(execute_many_to_many(conditions, texts, False)) == expected_results
