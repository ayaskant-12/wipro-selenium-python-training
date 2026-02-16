# Q1 What is the output?
# list(enumerate(['a', 'b', 'c']))
# A1
# [(0, 'a'), (1, 'b'), (2, 'c')]


# Q2 What is the output?
# for i, v in enumerate([10, 20, 30]):
#     print(i, v)
# A2  0 10
#     1 20
#     2 30

# Q3 Write code to print index + value from:
# colors = ['red', 'green', 'blue']
# Index should start from 1.
# A3
colors = ['red', 'green', 'blue']
for index,value in enumerate(colors, start=1):
    print(index, value)

# Q4 What is the output?
# list(enumerate("PYTHON", start=1))
# A4 [(1, 'P'), (2, 'Y'), (3, 'T'), (4, 'H'), (5, 'O'), (6, 'N')]

# Q5 Find the index of value 50 using enumerate():
# nums = [10, 20, 30, 40, 50, 60]
# A5
nums = [10, 20, 30, 40, 50, 60]
for index, value in enumerate(nums):
    if value==50:
        print(index, value)

# Q6 What is the output?
# for i, n in enumerate(range(10, 60, 10)):
#     print(i, n)
# A6  0 10
#     1 20
#     2 30
#     3 40
#     4 50

# Q7 Convert this into an enumerate() loop:
# for i in range(len(data)):
#     print(i, data[i])
# A7
# for i, value in enumerate(data):
#     print(i, value)

# Q8 What is printed?
# items = ['a', 'b', 'c']
# for i in enumerate(items):
#     print(i)
# A8
# (0, 'a')
# (1, 'b')
# (2, 'c')

# Q9 What is the output?
# list(enumerate([], start=5))
# A9 []

# Q10 What is the output?
# for i, v in enumerate([100, 200, 300], start=-1):
#     print(i, v)
# A10
# -1 100
# 0 200
# 1 300

# Q11 What happens here?
i, v = enumerate(['x', 'y', 'z'])
# error

# Q12 Explain the difference:
# enumerate(data) = it give the value pair in the order starting from 0
# enumerate(data, start=1) = it will give the value pair in the order starting from 1