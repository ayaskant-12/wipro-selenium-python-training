# generators - special type of functions - return one value a time, on demand
# yield -
# memory efficient
# usefull for large set of data
# files, retries, batching

# normal function
def numbers():
    return [1,2,3,4]
print(numbers())
# normal functions loads all the values into the memory

# generator function
def generator():
    print("printing 1")
    yield 1
    print("printing 2")
    yield 2
    print("printing 3")
    yield 3
    print("printing 4")
    yield 4
ret_val = generator()
print(next(ret_val))
print(next(ret_val))
print(next(ret_val))
