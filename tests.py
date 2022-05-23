from core.exceptions import ForsetiSyntaxError, ForsetiFunctionSyntaxError
from core.checkers import check_staples, check_syntax
from core.parse import parse_items
from core.execute import execute_automatically

import unittest


class TestChecker(unittest.TestCase):
	def test_check_staples(self):
		with self.assertRaises(ForsetiSyntaxError):
			check_staples("((True)")
			check_staples("(True))")

		self.assertIsNone(check_staples("(True)"))
		self.assertIsNone(check_staples("((True))"))
		self.assertIsNone(check_staples("True"))
		self.assertIsNone(check_staples("(True OR False) AND (False AND True)"))

	def test_check_syntax(self):
		with self.assertRaises(ForsetiSyntaxError):
			check_syntax("AND SomeCommand")
			check_syntax("SomeCommand AND")
			check_syntax("OR SomeCommand")
			check_syntax("SomeCommand OR")
			check_syntax("И SomeCommand")
			check_syntax("SomeCommand И")
			check_syntax("ИЛИ SomeCommand")
			check_syntax("SomeCommand ИЛИ")
			check_syntax("NOT SomeCommand")
			check_syntax("SomeCommand NOT")

		with self.assertRaises(ForsetiSyntaxError, msg="Operator 'NOT' cannot be used without operator 'AND'"):
			check_syntax("SomeCommand1 OR NOT SomeCommand2")
			check_syntax("SomeCommand1 NOT NOT SomeCommand2")
			check_syntax("SomeCommand1 NOT SomeCommand2")

	def test_condition_parser(self):
		with self.assertRaises(ForsetiSyntaxError, msg="The closing bracket is met before using the opening one"):
			parse_items("TRUE AND )FALSE(")
			parse_items("TRUE AND (()FALSE)()")

		self.assertListEqual(parse_items("TRUE AND ((FALSE))"), [['TRUE AND ', 'ATOM_1'], ['ATOM_2'], ['FALSE']])
		self.assertListEqual(
			parse_items("TRUE AND FALSE OR (TRUE AND (FALSE OR TRUE))"),
			[['TRUE AND FALSE OR ', 'ATOM_1'], ['TRUE AND ', 'ATOM_2'], ['FALSE OR TRUE']],
		)
		self.assertListEqual(
			parse_items("TRUE AND FALSE"),
			[['TRUE AND FALSE']],
		)


if __name__ == '__main__':
	unittest.main()
