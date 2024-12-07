def testDecorator(input_func):
    def output_func(*args):
        # extra logic
        count = len(args[0])
        print("-" * count)
        input_func(*args)
        print("-" * count)
        # extra logic

    return output_func


@testDecorator
def showMessage(text):
    print(text)


showMessage("Hello")
showMessage("Have a good day!")
