# -------------- generators
# yield vs return
def testYield():
    print("---1---")
    yield 1
    print("---2---")
    yield 2
    print("---3---")
    yield 3


# print(testYield())

for i in testYield():
    print(i)


# - 1,1,2,3,5,8,13...
def fibonacci_numbers(max):
    x, y = 1, 1
    while x <= max:
        yield x

        # if x % 7 == 0:
        #     break

        temp = y
        y = x + y
        x = temp


# for x in fibonacci_numbers(100):
#     input()  # pause
#     print(x)

# -------- Generator Expression Syntax
# print("-------------- Generator Expression")


def powOfTwo():
    for i in range(10):
        yield pow(2, i)


# syntax: [expresion, for var in collection (condition)]
result = [pow(2, i) for i in range(10)]

for i in powOfTwo():
    print(i, end=" ")

print("\n----- using gen exp")

for i in result:
    print(i, end=" ")
print("\n-----")


# get all even numbers from 0 to 100
def evenNumbers():
    for i in range(101):
        if i % 2 == 0:
            yield i
        if i >= 33 and i % 9 == 0:
            break


for i in evenNumbers():
    print(i, end=" ")
