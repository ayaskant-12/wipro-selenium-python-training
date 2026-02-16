# function is a block of code that performs specific task
# def functionname()

def printdata():
    print("Hello world")
# call the function
printdata()

# function with parameters
def printdata(name):
    print(f"Hello {name}")
# pass the argument
printdata("Tina")
printdata("Rita")
# return statement
# to return the function value we return the function statement
def squareroot(a):
    return a**0.5
# function call
print(f"squareroot is {squareroot(4)}")
# function pass
def fun_pass():
    pass
# call the function
fun_pass()
# multiple return values
def cal(a,b):
    return a-b, a+b,a*b
add, sub, mul = cal(10,5)
print(add,sub,mul)
# function calling a another function
def areaofrect(len, width):
    return len * width
def areaofsq(side):
    return side*side
value = areaofrect(4,6)
sq = areaofsq(value)
print(sq)

# function with a loop
def even(limit):
    for i in range(2, limit+1, 2):
        print(i)
even(10)

# function with if else condition
def even(limit):
    if limit%2==0:
        return "even"
    else:
        return "odd"
print(even(10))
print(even(11))

# 1.Write a Python function to sum all the numbers in a list.
def sum_list(a):
    sum = 0
    for i in a:
        sum += i
    return sum
a = [1,3,6,3,7,4,8,5,9,3,2,5,67]
print(sum_list(a))

# 2.Write a Python function to find the maximum of three numbers.
def maximum(a,b,c):
    return max(a,b,c)
print(maximum(2,5,4))