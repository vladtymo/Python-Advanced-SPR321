from abc import ABC, abstractmethod


# ------------ Figure ------------
class Figure(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self):
        pass

    def __str__(self) -> str:
        return self.name


# inheritamce: class Deriver(Base)
class Rectangle(Figure):
    def __init__(self, width, height) -> None:
        # super() - reference to base class
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # ----- operator overloading -----
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __gt__(self, other):
        return self.area() > other.area()

    def __round__(self, n=None):
        copy = Rectangle(self.width, self.height)

        if copy.width > copy.height:
            copy.width = copy.height
        else:
            copy.height = copy.width
        return copy

    def __str__(self) -> str:
        return f"{self.name}: {self.width}x{self.height}cm"

    def __int__(self) -> int:
        return self.area()


f1 = Rectangle(123, 88)
f2 = Rectangle(20, 30)
f3 = f1 + f2  # f1.__add__(f2)

print(f3)
print("Rectangle 1 > Rectangle 2: ", f1 > f2)
print("Rectangle 1 > Rectangle 2: ", f1 < f2)
print("Rectangle 1 > Rectangle 2: ", f1 == f2)

print(f"Area: {f1.area()}cm^2")
print(f"Area: {int(f1)}cm^2")

print("Rounded: ", round(f1))
