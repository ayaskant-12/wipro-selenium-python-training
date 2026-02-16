# Create a class Book with attributes title and author.
# Create 3 different book objects and print all details.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def print_details(self):
        print(f"the title is {self.title} and the author for the book is {self.author}")
book1 = Book('aya', 'byb').print_details()
book2 = Book('cyc', 'dyd').print_details()
book3 = Book('eye', 'fyf').print_details()

# Create a class Rectangle with a constructor that takes length and width and stores area and perimeter as object attributes.

class Rectangle:
    def __init__(self, length, width):
        self.area = length*width
        self.perimeter = 2 * (length+width)
    def print_details(self):
        print(f"the area of the rectangle is {self.area}\nthe perimeter of the rectangle is {self.perimeter}")
rect = Rectangle(23,45).print_details()