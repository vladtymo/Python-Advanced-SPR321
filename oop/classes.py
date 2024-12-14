from datetime import datetime


class Order:

    # static fields
    initial_number = 1000

    # constructor (self = this)
    def __init__(self, title, price, discount):
        # set fields
        self.name = title
        # __name - private field
        self.__price = price
        self.discount = discount

        self.number = Order.initial_number
        Order.initial_number += 1

        self.creationDate = datetime.now()

    def __del__(self):
        # clear unmanaged resources
        print("---- Order destructor ----")

    def show(self):
        print(
            f"Order info: {self.name} - {self.__price}$ create at {self.creationDate.strftime("%d/%m/%Y")}"
        )

    # ------ getter & setter ------
    def getPrice(self):
        return self.__price

    def setPrice(self, value):
        self.__price = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value

    # ------ magic method ------
    def __str__(self):
        return f"#{self.number}: {self.name} - {self.__price}$"

    def __int__(self):
        return self.number


order1 = Order("iPhone 13 Pro", 690, 5)
order1.show()

order2 = Order("Marshall Major IV", 99, 15)
order2.show()

print(order1)
print(int(order1))

# ---- get & set
order1.setPrice(550)
print(f"Price: {order1.getPrice()}$")

order1.price = 440
order1.price = -120  # ignore
print(f"Price: {order1.price}$")

order3 = Order("JBL Charge 3", 49, 5)

print(order1)
print(order2)
print(order3)


# ---------- inheritance ----------
class SuperOrder(Order):
    def __init__(self, name, price, discount, bonus):
        # set base properties
        super().__init__(name, price, discount)
        # create new properties
        self.bonus = bonus

    def __str__(self):
        return f"I am super order #{self.number}"


superOrder = SuperOrder("Vision Pro", 3499, 0, 333)

print(superOrder)  # __str__()
