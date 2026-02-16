# Write a Python program to get the largest number from a list.

numbers = [12, 45, 7, 89, 23, 34, 78]
print("Largest number:", max(numbers))


# remove the even numbers from the lost
numbers = [12, 45, 7, 89, 23, 34, 78]
odd = []
for i in numbers:
    if i%2!=0:
        odd.append(i)
print(odd)

# multiply the items in the list
numbers = [12, 45, 7, 89, 23, 34, 78]
result = 1
for i in numbers:
    result *= i
print(f"the product of all the elements in the list is {result}")
