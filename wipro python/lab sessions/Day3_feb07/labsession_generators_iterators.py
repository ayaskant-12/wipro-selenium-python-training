# Create a custom iterator that prints numbers from 1 to 5.
count = 1
def next_number():
    global count
    if count <= 5:
        value = count
        count += 1
        return value
it = iter(next_number, None)
for num in it:
    print(num)
# Write an iterator class that returns next even number.
even = 0
def next_even():
    global even
    even += 2
    if even <= 10:
        return even
it = iter(next_even, None)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# Explain and demonstrate the use of __iter__() and __next__().
# __iter__() - Initializes and returns the iterator object
# __next__() - Returns the next value in sequence


# Write a generator to generate numbers from 1 to N.
def numbers(n):
    for i in range(1, n + 1):
        yield i
for num in numbers(5):
    print(num)
# Create a generator to generate even numbers only.
def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i
for e in even_numbers(10):
    print(e)
# Write a generator to read a file line by line.
def read_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line
for line in read_file("text.txt"):
    print(line.strip())
# Create a generator for Fibonacci series.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for f in fibonacci(7):
    print(f)
# Write a generator that simulates retry attempts (max 3 tries).
def retry_attempts(max_retries=3):
    attempt = 1
    while attempt <= max_retries:
        yield f"Attempt {attempt}"
        attempt += 1
for attempt in retry_attempts():
    print(attempt)