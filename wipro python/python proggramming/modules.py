# module is a file that ontains python code
# benefits
# code reusability, easier maintainance
# better organization
# built in modules
# user defined modules
# buillt in modules - math, os, sys, datetime, random, json

# import math
# from datetime import datetime
# from datetime import date
# print(math.sqrt(16))
# print(math.pi)
# print(datetime.now())
# print(datetime.now().day)
# print(date.today())




def make_it_equal(A, B):

    if A is None or B is None:
        return -1

    if '%' not in A:
        return "" if A == B else -1

    parts = A.split('%', 1)
    prefix = parts[0]
    suffix = parts[1]

    if not B.startswith(prefix):
        return -1

    if not B.endswith(suffix):
        return -1

    start = len(prefix)
    end = len(B) - len(suffix)

    if start > end:
        return -1

    return B[start:end]


# non editable starts here
if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    print(make_it_equal(A, B))
# non editable ends here