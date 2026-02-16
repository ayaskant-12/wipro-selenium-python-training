# function - function name, arguments, return type, code
# lamba functions - anonymous (nameless) functions, one line, simple operations
# syntax     ->      lambda arguements: expressions
# it can have any number of arguements
# must have only one expression
# expression is automatically returned

# normal function for adding 2 numbers
def add(a,b):
    return a+b
print(add(5,3))
# lambda function for adding 2 numbers
add =lambda a,b: a+b
print(add(5,3))
# lambda function for square of a number
square = lambda x: x*x
print(square(5))
# lambda function to check whether even or odd
even = lambda x: x%2==0
print(even(3))
# lambda function to find the max of 2 numbers
max = lambda a,b: a if a > b else b
print(max(10,30))


# filter,map and reduce in built functions in lambda
# filter - select data - filtering the data
# map - transform the data
# reduce - aggregate the data


# filter
numbers = [1,2,3,4,5,6]
evens = list(filter(lambda x: x%2==0, numbers))
print(evens)
# filter the failed test cases
status = ['pass', 'fail', 'pass', 'fail']
failed = list(filter(lambda s: s=='fail', status))
print(failed)
# filter +ve numbers
nums = [-5, 10, -3, 7, 0, 2]
pos = list(filter(lambda n: n>=0, nums))
print(pos)
# filter non empty strings
data = ["hello", "", "world", "", "python"]
non_empty = list(filter(lambda d: d!="", data))
print(non_empty)


# reduce - aggregate - combining many values to a one single result
from functools import reduce
nums = [10,20,30,40]
# addition
print(reduce(lambda  x,y: x+y, nums))
# multiply
print(reduce(lambda x,y: x*y, nums))
# max value
print(reduce(lambda x, y: x if x > y else y, nums))
# min value
print(reduce(lambda x, y: x if x < y else y, nums))


# map - transform the data
nums = [10,20,30,40]
# square
squares = list(map(lambda x:x**2, nums))
print(squares)


# sorting in lambda
data = [(1,3), (4,1), (2,2)]
sortdata = sorted(data, key=lambda x:x[1])
print(sortdata)

marks = {'A': 75, 'B': 90, 'C': 60}
sort_marks = dict(sorted(marks.items(), key=lambda x:x[1]))
print(sort_marks)