from abc import ABC, abstractmethod
import math

class LogsMixin:
    def log(self, message):
        print(f"[LOG]: {message}")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape, LogsMixin):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.width * self.length
        self.log(f"Calculated area of rectangle: {result}")

    def perimeter(self):
        result = 2 * (self.length + self.width)
        self.log(f"Calculated perimeter of rectangle: {result}")

class Circle(Shape, LogsMixin):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = math.pi * self.radius**2
        self.log(f"Calculated area of circle: {result}")

    def perimeter(self):
        result = 2 * math.pi * self.radius
        self.log(f"Calculated perimeter of circle: {result}")

if __name__ == "__main__":
    rect = Rectangle(length=10, width=5)
    rect.area()
    rect.perimeter()

    circ = Circle(radius=5)
    circ.area()
    circ.perimeter()
