vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# index of 'e'
index = vowels.index('e')
print('The index of e:', index)
# index of the first 'i'
index = vowels.index('i')
print('The index of i:', index)


theList = ['a', 'i', 'e', 'o', 'u']
theList.sort(reverse=True)
print(theList)


theList = ['a', 'e', 'i', 'o', 'u']
newList = sorted(theList, reverse=True)
print("Original list:", theList, "Memory addr:", id(theList))
print("Copy of the list:", newList, "Memory addr:", id(newList))
