# 1.Write a Python function to check whether a number falls within a given range.

a = int(input("enter the number: "))
if a in range(10):
    print("yes")
else:
    print("no")

# 2. Write a Python function to Print even numbers from 1 to 50

a = range(2,51,2)
for i in a:
    print(f"{i}")

# 3. Write a Python function to Sum of numbers from 1 to 100

a = range(1,101)
sum = 0
for i in a:
    sum+=i
print(sum)

# 4. Print all numbers divisible by 5 between 1 and 100

a = range(1,101)
for i in a:
    if i % 5 == 0:
        print(f"{i}")

# 5.Create a list of numbers from 50 to 100 with a step of 5

a = range(50,101,5)
lst = []
for i in a:
    lst.append(i)

# 6. Print the square of each number from 1 to 10.

a = range(1,11)
for i in a:
    print(i**2)

# 7. Print numbers between -10 and 10.

a = range(-10, 11)
for i in a:
    print(i)