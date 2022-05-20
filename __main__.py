from core.checkers.all_ import check_all
from core.parse_condition_items import parse_items
from core.command_execute import execute_condition


if __name__ == "__main__":
    while True:
        condition = input("Condition: ")
        text = input("Text: ").lower()

        try:
            check_all(condition)
            prepared_condition = parse_items(condition)
            res = execute_condition(prepared_condition, text)
            print("Result:", res)

        except Exception as err:
            print("Error:", err)
