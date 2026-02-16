# constructors - first function of the class called when an object of the class is created
# syntax __init__()
# we can parametrized the constructors
# self is mandatory

class student:
    def __init__(self):
        print("Constructor is called")
    def addsum(self):
        print("Adding 2 numbers")
s1 = student()
s1.addsum()

# parametrized constructors
# self.name is a instance variable or a global variable(belongs to the object
# name is a local variable parameter(exists inside the method)
# if we dont assign it to the self.name the object will not remember the value
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def printing(self):
        print(self.name)
        print(self.salary)
e1 = Employee('aya', 900000).printing()
e2 = Employee('byb', 700000).printing()

# using * args i constructor
# constructor overloading is supported by *args keyword
# we can pass any number of parameter to the constructor using *args

class Numbers:
    def __init__(self, *args):
        self.values = args
n = Numbers(10,20,30)
print(n.values)
m = Numbers(3,4)
print(m.values)
p = Numbers(3)
print(p.values)

# parent and child constructors
# super keyword for accessing parent constructor
#  calling parent constructor using super()
class Parent:
    def __init__(self):
        print("I am the parent constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am the child constructor")

c = Child()