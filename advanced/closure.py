def outer():

    # closure data
    number = 1

    # closure function
    def inner():
        nonlocal number  # get variable from outer score
        print(number)
        number += 1

    return inner


func = outer()

func()
func()
func()


# 1,1,2,3,5,8,13...
def fibonacci_numbers():

    # closure data
    x, y = 1, 1

    # closure function
    def inner():
        nonlocal x, y  # get variable from outer score
        print(x)
        sum = x + y
        x = y
        y = sum

    return inner


next = fibonacci_numbers()

for i in range(10):
    next()
