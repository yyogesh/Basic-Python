for x in range(10):
    print(x)

print("Range loop".center(50, '*'))

for x in range(4, 10):
    print(x)


print("Range loop".center(50, '*'))

for i in range(1, 10):
    print("No {} squared is {} and cubed is {} ".format(i, i**2, i**3))


language = ['Hindi', 'English', 'Sanskrit']

for lang in language:
    print(lang)


for x in 'python':
    print(x)


numbers = [1, 5, 9, 20, 100, 34, 87]

sum = 0

for no in numbers:
    sum = sum + no


print('Sum is ', sum)


for x in range(0, 10, 2):
    print(x)

language = ['Hindi', 'English', 'Sanskrit']
for i in range(len(language)):
    print(i, language[i])


number = "9,223,332,036,854,775,807"

for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i])

print("Get Numer ".center(50, '*'))

for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')

print("Get Numer ".center(50, '*'))

number = "9,223,332,036,854,775,807"

for i in range(0, len(number)):
    if number[i] == '0':
        break
    print(number[i])

print("Get Numer ".center(50, '*'))

for i in range(0, len(number)):
    if number[i] == ',':
        continue
    print(number[i], end='')


for i in range(1, 15):
    for j in range(1, 11):
        print('{1} times {0} is {2}'.format(i, j, i * j))
    print("Get Numer ".center(50, '*'))
else:
    print("Well done !")
