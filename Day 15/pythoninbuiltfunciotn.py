integer = -20
print(abs(integer))


# list = [1, 2, 3]
# print(any(list))

# list = [0, 0, False]
# print(any(list))


# list = [0, 0, False, 3]
# print(any(list))

# list = []
# print(any(list))

#  The all() method returns True when all elements in the given iterable are true. If not, it returns False.


# list = []
# print(all(list))

# list = [0, 0, False, 3]
# print(all(list))

# list = [1, 2, 3]
# print(all(list))


normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))


number = 5
print(bin(number))

print(bool(number))

# [] false , [0] true, 0.0 false, True true , 'asdf' true

str = "python is good language"

slice_obj = slice(3)
print(str[slice_obj])

slice_obj = slice(2, 6, 2)
print(str[slice_obj])


numbers = [2, 3, 5 - 10, 19]

print(sum(numbers))

number_list = [1, 2, 3, 5]
str_list = ['one', 'two', 'three', 'five']

result = zip()
resutl_lsit = list(result)
print(resutl_lsit)


result = zip(number_list, str_list)
print(tuple(result))

print(dir(number_list))
print(dir())
