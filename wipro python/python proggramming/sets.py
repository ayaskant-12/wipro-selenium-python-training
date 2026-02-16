std_id = {112, 113, 114, 115, 115}
print(std_id)

letters = {'a', 'b', 'c', 'd', 'e'}
print(letters)

mixed_set = {'Hello', 1, -7, 8, 9}
print(mixed_set)

empty_set = set()
print(empty_set)

mixed_set.add('ayaskant')
print(mixed_set)
mixed_set.pop()
print(mixed_set)
mixed_set.remove(8)
print(mixed_set)

a = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
b = {'c', 'd', 'e', 'f', 'h', 'i'}
print(a.difference(b))
a.difference_update(b)
print(a)

a = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
b = {'c', 'd', 'e', 'f', 'h', 'i'}
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.union(b))
print(a.intersection(b))
print(a.isdisjoint(b))