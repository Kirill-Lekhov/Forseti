from core.checkers import check_staples, check_syntax

import unittest


class TestChecker(unittest.TestCase):
	def test_check_staples(self):
		with self.assertRaises(AssertionError):
			check_staples("((True)")
			check_staples("(True))")

		self.assertIsNone(check_staples("(True)"))
		self.assertIsNone(check_staples("((True))"))
		self.assertIsNone(check_staples("True"))
		self.assertIsNone(check_staples("(True OR False) AND (False AND True)"))

	def test_check_syntax(self):
		with self.assertRaises(SyntaxError):
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

		with self.assertRaises(SyntaxError, msg="Оператор 'NOT' не может использоваться без оператора 'AND'"):
			check_syntax("SomeCommand1 OR NOT SomeCommand2")
			check_syntax("SomeCommand1 NOT NOT SomeCommand2")
			check_syntax("SomeCommand1 NOT SomeCommand2")


if __name__ == '__main__':
	unittest.main()
