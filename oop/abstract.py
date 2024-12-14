from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} says {self.make_sound()}"


class Dog(Animal):

    def make_sound(self):
        return "Gav-gav"


class Cat(Animal):

    def make_sound(self):
        return "Meow-meow"


# Example usage
dog = Dog("Rex")
cat = Cat("Tom")
print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow

print(dog)  # Output: Bark
print(cat)  # Output: Meow


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

    def __str__(self) -> str:
        return f"{self.name}: {self.width}x{self.height}cm"

    def area(self):
        return self.width * self.height


def show_figure(figure: Figure):
    print(f"Figure: {figure}")
    print(f"Area: {figure.area()}cm^2")


f1 = Rectangle(123, 88)

print(f1)
print(f"Area: {f1.area()}cm^2")

# в якості типу Figure можна передати будь-який клас, який успадковує Figure
show_figure(f1)

# error with creating Figure with abstract methods
# figure = Figure("Figure")
