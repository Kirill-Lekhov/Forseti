from .core.execute import execute_condition


if __name__ == "__main__":
    while True:
        condition = input("Condition: ")
        text = input("Text: ")

        if not any((condition, text)):
            print("Thanks for using!")
            exit(0)

        try:
            res = execute_condition(condition, text)
            print("Result:", res)

        except Exception as err:
            print("Error:", err)
