# Questions
# 1.Handle FileNotFoundError Exception When Opening a File

import json

try:
    with open("data.json", "r") as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print("Error: JSON file not found.")

# 2. Write a program to handle invalid user input
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# 3.Write a Python program that generates random alphabetical characters,
# alphabetical strings, and alphabetical strings of a fixed length.
# Use random.choice()
import random
import string
try:
    length = int(input("Enter length of the string: "))
    if length <= 0:
        raise ValueError("Length must be positive")
    char = random.choice(string.ascii_letters)
    rand_string = ''.join(
        random.choice(string.ascii_letters)
        for _ in range(random.randint(3, 10))
    )
    fix_string = ''.join(
        random.choice(string.ascii_letters)
        for _ in range(length)
    )
    print("Random character:", char)
    print("Random string:", rand_string)
    print("Fixed length string:", fix_string)
except ValueError as e:
    print("Invalid input:", e)
