from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Subclass 1 implementing the abstract methods
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Subclass 2 implementing the abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating instances of the subclasses
rect = Rectangle(10, 5)
circle = Circle(7)

# Demonstrating abstraction with implemented methods
print(f"Rectangle Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"Circle Area: {circle.area()}, Perimeter: {circle.perimeter()}")
