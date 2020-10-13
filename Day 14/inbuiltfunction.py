integer = -20
print('Absolute value of -20 is:', abs(integer))

# random floating number
floating = -30.33
print('Absolute value of -30.33 is:', abs(floating))

# Absolute value of - 20 is: 20
# Absolute value of - 30.33 is: 30.33


# True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
print(any(l))

# False since both are False
l = [0, False]
print(any(l))

# True since 5 is true
l = [0, False, 5]
print(any(l))

# False since iterable is empty
l = []
print(any(l))


# all values true
l = [1, 3, 4, 5]
print(all(l))

# all values false
l = [0, False]
print(all(l))

# one false value
l = [1, 3, 4, 0]
print(all(l))

# one true value
l = [0, False, 5]
print(all(l))

# empty iterable
l = []
print(all(l))


normalText = 'Python is interesting'
print(ascii(normalText))

otherText = 'Pythön is interesting'
print(ascii(otherText))

print('Pyth\xf6n is interesting')

# 'Python is interesting'
# 'Pyth\xf6n is interesting'
# Pythön is interesting


number = 5
print('The binary equivalent of 5 is:', bin(number))
# The binary equivalent of 5 is: 0b101

test = []
print(test, 'is', bool(test))

test = [0]
print(test, 'is', bool(test))

test = 0.0
print(test, 'is', bool(test))

test = None
print(test, 'is', bool(test))

test = True
print(test, 'is', bool(test))

test = 'Easy string'
print(test, 'is', bool(test))

# [] is False
# [0] is True
# 0.0 is False
# None is False
# True is True
# Easy string is True


py_string = 'Python'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3)
print(py_string[slice_object])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
print(py_string[slice_object])   # yhn


numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)

# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)
