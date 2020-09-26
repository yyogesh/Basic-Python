# ipAddress = input("Please enter an ip address : ")
# print(ipAddress.count('.'))


toppings = ['pepperoni', 'sausage', 'mushroom', 'sausage']
print(toppings.count('sausage'))

odd = [2, 4, 6, 8]

odd[0] = 1

print(odd)

print(odd[1:4])

odd[1:4] = [3, 5, 7]
print(odd)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
print(numbers)
x = sorted(numbers)
print(x)


print(['Hello'] * 3)

my_list = [1, 2, 3]
my_list.append("Hello")

print(my_list)

my_list.append([1, 2, 3])
print(my_list)

my_list.append({'a': 4, 'b': 6})
print(my_list)

print('*' * 50)

my_list = [1, 2, 3]
my_list.extend("Hello")

print(my_list)

my_list.extend([1, 2, 3])
print(my_list)

my_list.extend({'a': 4, 'b': 6})
print(my_list)

for item in my_list:
    print(item)


my_list.insert(4, 100)
print(my_list)


my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# delete one item
del my_list[2]

print(my_list)

del my_list[1:5]
print(my_list)

# del my_list
# print(my_list)


my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm', 'p', 'o', 'p', 'm']

my_list.remove('p')
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(3))
print(my_list)

my_list.clear()
print(my_list)


my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
my_list[2:4] = []
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for item in numbers:
    print(item)
    for value in item:
        print(value)
