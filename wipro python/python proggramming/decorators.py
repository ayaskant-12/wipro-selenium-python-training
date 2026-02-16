# decorators - wrapper function around the functions are called as decorators
# decorator
# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         func()
#     return inner
# @make_pretty
# def vanillacake():
#     print("I am the vanilla cake")
# @make_pretty
# def strawberrycake():
#     print("I am the strawberry cake")
#
# vanillacake()
# strawberrycake()
#



nums = [1, 2, 3, 4]
print(list(map(lambda x: x % 2 == 0, nums)))
