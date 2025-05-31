def withBorders(input_func):
    def output_func(*args):
        count = 10
        if isinstance(args[0], str):
            count = len(args[0]) - 2
        print(f"┏{"*" * count}┓")
        # extra logic
        input_func(*args)
        # extra logic
        print(f"┗{"*" * count}┛")

    return output_func


@withBorders
def showMessage(text):
    print(text)

showMessage("Hello")
showMessage("Have a good day!")
showMessage("How are you doing today?")
showMessage("See you later!")