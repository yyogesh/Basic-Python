def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<


print(sum_numbers)


def higher_order_function(f, *args):  # function as a parameter
    summation = f(*args)
    return summation


result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15


def square(x):          # a square function
    return x ** 2


def cube(x):            # a cube function
    return x ** 3


def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)


def higher_order_function(type):  # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3


# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable


def is_even(num):
    if num % 2 == 0:
        return True
    return False


even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]


numbers = [1, 2, 3, 4, 5]  # iterable


def is_odd(num):
    if num % 2 != 0:
        return True
    return False


odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]


# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable


def is_name_long(name):
    if len(name) > 7:
        return True
    return False


long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
