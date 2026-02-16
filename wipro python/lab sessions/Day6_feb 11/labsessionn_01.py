# Write a regex to check if a string contains only digits.

import re
text = input("Enter a string: ")
if re.fullmatch(r"\d+", text):
    print("contains only digits")
else:
    print("dosnt contains only digits")

# Write a pattern to match a 10-digit mobile number.

mobile = input()
if re.fullmatch(r"\d{10}", mobile):
    print("valid mobile number")
else:
    print("not valid")

# Find all lowercase letters in a string.

text = input()
lowercase_letters = re.findall(r"[a-z]", text)
print(lowercase_letters)

# Extract all uppercase letters from a sentence.

text = input()
uppercase_letters = re.findall(r"[A-Z]", text)
print(uppercase_letters)

# Match a string that starts with "Hello".

text = input()
if re.match(r"^Hello", text):
    print("starting with hello")
else:
    print("not starting with hello")

# Match a string that ends with "world".

text = input()
if re.search(r"world$", text):
    print("ends with world")
else:
    print("not ends with world")

# Find all words separated by spaces.

text = input()
words = re.findall(r"\w+", text)
print(words)

# Match exactly 5 characters.

text = input()
if re.fullmatch(r".{5}", text):
    print("has 5 characters")
else:
    print("not have 5 characters")

# Find all occurrences of the word "python" (case-sensitive).

text = input()
matches = re.findall(r"python", text)
print(matches)

# Replace all spaces in a string with underscores.

text = input()
result = re.sub(r"\w", "_", text)
print(result)