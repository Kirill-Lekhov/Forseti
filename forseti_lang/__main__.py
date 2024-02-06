from forseti_lang.execute import execute_condition

from sys import exit


def main() -> int:
	print("Welcome to Forseti! To exit, keep silent twice.")

	while True:
		condition = input("Condition: ")
		text = input("Text: ")

		if not condition or not text:
			print("Thanks for using!")
			return 0

		try:
			print("Result:", execute_condition(condition, text))

		except Exception as err:
			print("Error:", err)


if __name__ == "__main__":
	exit(main())
