from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


rect = Rectangle(10, 20)
circle = Circle(5)
square = Square(7)

print(f"Rectangle's area = {rect.area()}, perimeter = {rect.perimeter()}")
print(f"Circle's area = {circle.area()}, perimeter = {circle.perimeter()}")
print(f"Square's area = {square.area()}, perimeter = {square.perimeter()}")
