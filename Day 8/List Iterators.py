theList = ['a', 'i', 'e', 'o', 'u']

my_itr = iter(theList)

for i in range(0, len(theList)):
    print(next(my_itr))

print(next(my_itr))
print(next(my_itr))
