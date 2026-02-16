# exceptions - runtime errors which will disrupt the normal program flow
# benefits
# helps in debugging
# prevents program crashing
# handling errors and exceptions in the code more efficiently

# try except

# try - code to be executed
# except - exceptions details catching
# else: if the exception does not occur then else part will be executed
# finally - mandated code
# custom exceptions

try:
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by 0")
except ValueError:
    print("enter valid numbers")

# generic exception
try:
    a = 5/0
except Exception as e:
    print(e)
# runs only if no exception occurs
else:
    print("Division successful")
# mandatory code
finally:
    print("Close the browser")
# custom exceptions - creating a own exception
# age = int(input("enter the age"))
# if age < 18:
#     raise ValueError("Age must be 18 or above")


