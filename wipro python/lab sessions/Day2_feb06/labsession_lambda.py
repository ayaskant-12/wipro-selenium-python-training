from functools import reduce
# Q1
# From a list of numbers:
nums = [1, 2, 3, 4, 5, 6]
#   Filter even numbers
even = list(filter(lambda x:x%2==0, nums))
print(even)
#   Square them
square = list(map(lambda x:x**2, even))
print(square)
#   Find their sum
total = reduce(lambda  x,y: x+y, square)
print(total)

# Q2
# from a list of salaries:
salaries = [25000, 40000, 32000, 18000]
#       Filter salaries > 30,000
fil = list(filter(lambda x:x>30000, salaries))
print(fil)
#       Add 10% hike
hike = list(map(lambda x:x + (x*0.1), fil))
print(hike)
#       Find the total payout
total2 = reduce(lambda x,y: x+y, hike)
print(total2)

# Q3  Write a Python program to sort a list of tuples using Lambda
# Q4  Write a Python program to extract year, month, date and time using Lambda.

