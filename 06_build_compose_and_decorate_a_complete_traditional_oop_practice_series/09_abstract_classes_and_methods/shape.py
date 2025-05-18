from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

# Subclass that implements the abstract method
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Create object and call area
rect = Rectangle(5, 3)
print("Area of rectangle:", rect.area())
