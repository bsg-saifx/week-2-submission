from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.width*self.length

    def perimeter(self):
        return 2*(self.length+self.width)

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return 2*math.pi*self.radius

if __name__=="__main__":
    rect = Rectangle(length=10,width=5)
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")

    circ = Circle(radius=5)
    print(f"Area : {circ.area()}")
    print(f"Perimeter: {circ.perimeter()}")
