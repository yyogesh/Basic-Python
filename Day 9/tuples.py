# create an empty tuple
py_tuple = ()
# list = []
print("A blank tuple:", py_tuple)

# create a tuple without using round brackets
py_tuple = 33, 55, 77
print("A tuple set without parenthesis:", py_tuple, "type:", type(py_tuple))

# create a tuple of numbers
py_tuple = (33, 55, 77)
print("A tuple of numbers:", py_tuple)

# create a tuple of mixed numbers
# such as integer, float, imaginary
py_tuple = (33, 3.3, 3+3j)
print("A tuple of mixed numbers:", py_tuple)

# create a tuple of mixed data types
# such as numbers, strings, lists
py_tuple = (33, "33", [3, 3])
print("A tuple of mixed data types:", py_tuple)

# create a tuple of tuples
# i.e. a nested tuple
py_tuple = (('x', 'y', 'z'), ('X', 'Y', 'Z'))
print("A tuple of tuples:", py_tuple)


# A blank tuple: ()
# A tuple set without parenthesis: (33, 55, 77) type: <class 'tuple'>
# A tuple of numbers: (33, 55, 77)
# A tuple of mixed numbers: (33, 3.3, (3+3j))
# A tuple of mixed data types: (33, '33', [3, 3])
# A tuple of tuples: (('x', 'y', 'z'), ('X', 'Y', 'Z'))


# A single element surrounded by parenthesis will create a string instead of a tuple
py_tuple = ('single')
type(py_tuple)
# <class 'str' >
# You need to place a comma after the first element to create a tuple of size "one"
py_tuple = ('single',)
type(py_tuple)
# <class 'tuple' >
# You can use a list of one element and convert it to a tuple
py_tuple = tuple(['single'])
type(py_tuple)
# <class 'tuple' >
# You can use a set of one element and convert it to a tuple
py_tuple = tuple({'single'})
type(py_tuple)
# <class 'tuple' >

weekdays = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
print(weekdays)
# ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
# accessing elements leaving the first one
print(weekdays[1:])
('tue', 'wed', 'thu', 'fri', 'sat', 'sun')
# accessing elements between the first and fifth positions
# excluding the ones at the first and fifth position
print(weekdays[1:5])
('tue', 'wed', 'thu', 'fri')
# accessing elements after the fifth position
print(weekdays[5:])
('sat', 'sun')
# accessing the first five elements
print(weekdays[:5])
('mon', 'tue', 'wed', 'thu', 'fri')
# accessing elements that appears after
# counting five from the rear end
print(weekdays[:-5])
('mon', 'tue')
# accessing five elements from the rear
print(weekdays[-5:])
('wed', 'thu', 'fri', 'sat', 'sun')
# accessing elements from the start to end
print(weekdays[:])
('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')


py_tuple = (22, 33, 55, 66, [88, 99])
print("Tuple before modificaton:", py_tuple)

# Let's try to modify py_tuple
# It'll return a TypeError
# try:
# py_tuple[0] = 11
# except Exception as ex:
# print("OP(py_tuple[0]) Error:", ex)

# We can change the values of mutable
# elements inside the py_tuple i.e. list
py_tuple[4][0] = 77
py_tuple[4][1] = 88
print("Tuple after modificaton:", py_tuple)

# We can assign a tuple with new data
py_tuple = ('mon', 'tue', 'wed')
print("Tuple after reassignment:", py_tuple)

py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
print("First Test: Does 'p' exist?", 'p' in py_tuple)
# First Test: Does 'p' exist? True
print("Second Test: Does 'z' exist?", 'z' in py_tuple)
# Second Test: Does 'z' exist? False
print("Third Test: Does 'n' exist?", 'n' in py_tuple)
# Third Test: Does 'n' exist? True
print("Last Test: Does 't' not exist?", 't' not in py_tuple)
# Last Test: Does 't' not exist? False

py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
for item in py_tuple:
    print("Item:", item)

# Item: p
# Item: y
# Item: t
# Item: h
# Item: o
# Item: n


emp_records = ('john', 'hr', 2010, 'robert',
               'account', 2015, 'bill', 'mis', 2018)
(emp_name, emp_dept, emp_join_date) = emp_records[0:3]
print(emp_name)
# 'john'
print(emp_dept)
# 'hr'
print(emp_join_date)
# 2010


tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 == tuple2)    # False
print(tuple1 < tuple2)      # True
print(tuple1 > tuple2)      # False
