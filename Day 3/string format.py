print('test hello my name {0}'.format('abc'))

print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))

print('{} {} cost ${}'.format(6, 'bananas', 1.74))


print('{2} {0} cost ${1}'.format(6, 'bananas', 1.74))

print('{quantity} {a} cost ${b}'.format(quantity=6, a='apple', b='1.74'))

age = 24
print("My age is {} year".format(age))

print("There are {0} days in {1}".format(31, 'January'))


print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}".format(
    31, "January", "March", "May", "July", "August", "October", "December"))


print("""Janary : {2} 
February: {0}
March: {2}
April : {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28, 30, 31))
