# 1.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(5)
print("Area: ", c.area())
print("Perimeter: ", c.perimeter())

# 2.Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date
class Person:
    def __init__(self, name, country, year, month, day):
        self.name = name
        self.country = country
        self.dob = date(year, month, day)
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
p = Person("Aya", "India", 2003, 3, 16)
print("Age: ", p.age())

# 3.Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
sq = Square(4)
print("Square Area: ", sq.area())
triangle = Triangle(12,34,56)
print("Triangle area: ", triangle.area())

# 4.Write a python program to create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def show(self):
        print("Vehicle Name: ", self.name)
        print("Speed: ", self.speed)
class Bus(Vehicle):
    pass
b = Bus("School Bus", 60)
b.show()

# 5.Write a python program to create  a Vehicle class without any variables and methods

class Vehicle:
    pass
v = Vehicle()
print("object created")