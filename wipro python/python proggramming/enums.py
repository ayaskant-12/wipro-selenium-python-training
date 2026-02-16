# enumerate with list values
fruits = ["orange", "Cherry", "Kiwi"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
print("\n\n")


# enumerate with start value changed
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
print("\n\n")

# enumerate with strings
word = "python"
for i, ch in enumerate(word, start=1):
    print(i, ch)
print("\n\n")

# enumerate with tuples
tup = ("ayaskant", "int", "float", "str")
for index, top in enumerate(tup):
    print(index, top)
print("\n\n")

# real time scenerio
test_cases = ["Login", "Signup", "Checkout"]
for case_number, test in enumerate(test_cases, start=1):
    print(f"Executing Testcase {case_number}: {test}")
print("\n\n")

# accessing of the enumerate values

a = ['God', 'is', 'Great']
b = enumerate(a)
nxt_val = next(b)
nxt_val = next(b)
nxt2_val = next(b)
print(nxt_val)
print(nxt2_val)
print("\n\n")

# duplicate detection using enumeration
characters = ["Krillin", "Goku", "Goku", "Gohan", "Piccolo",
              "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
              "Piccolo", "Goku", "Vegeta", "Goku", "Piccolo"]
character_map = {character: [] for character in set(characters)}
for index, character in enumerate(characters):
    character_map[character].append(index)
print(character_map)
print("\n\n")