empty_list = []
numbers = [1,2,3,4]
mixeddata = [1, "hello", True, 6.67, 1]
nested = [[1,2], [3,4]]

print(mixeddata[1])
print(mixeddata[2])

mixeddata[4] = 6
print(mixeddata)

mixeddata.insert(0,10)
print(mixeddata)

mixeddata.append("John")
print(mixeddata)

mixeddata.remove("hello")
print(mixeddata)

mixeddata.pop()
print(mixeddata)
mixeddata.pop(1)
print(mixeddata)


numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(3))
print(numbers.index(3))
numbers.clear()

fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

for i, fruit in enumerate(fruits):
    print(i, fruit)

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list = ", my_list)

print(my_list[2:5])
print(my_list[5:])
print(my_list[:])
numbers = [1,3,5]
even_number = [2,4,6]
numbers.extend(even_number)
print(numbers)

