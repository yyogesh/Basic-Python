# SET no duplicate immutable (you can not change) order
my_set = {3, 2, 3, 'hello', (1, 2, 3)}
print(my_set)

my_set = {5, 2, 3, 'hello', (1, 2, 3)}
print(my_set)


my_set = set([1, 2, 3])

print(my_set)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])

print(wild_animals)
for animal in wild_animals:
    print(animal)

wild_animals.add('xyz')
print(wild_animals)

wild_animals.remove('xyz')
print(wild_animals)

even = set(range(0, 40, 2))
squares_tuple = (4, 6, 9, 16, 25)
print(even.union(set(squares_tuple)))
print(even.intersection(set(squares_tuple)))


print(sorted({100, 2, 20, 200, 98, 65}))
