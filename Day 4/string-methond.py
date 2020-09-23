# ASCII value
print(ord('N'))

print(chr(78))

print(max('python'))
print(min('python'))

print(len('python'))  # length of string

print(' python')
print(' python '.strip())

print(' python is really gud language'.lstrip())

print(' python is really gud language ' + ' ' + 'after strip')
print(' python is really gud language '.rstrip() + ' ' + 'after strip')


print('Python'.lower())
print('Python'.upper())

print('Python'.replace('y', 'x'))

print('Python, language'.split(','))

print('Python language'.split())

print('Python@gmail.com'.split('@'))

print('Python@gmail@com'.split('@'))

print('Python@gmail@com'.split('@', 1))

print('python@language'.partition('@'))

print('python@language'.partition('$'))

print('python is really good language'.title())

print('python is really good language capitalize'.capitalize())

print('python'.isalpha())

print('pytho12n'.isalnum())

print(' '.isspace())

print('python is top language'.startswith('python'))

print('python is top language'.endswith('language'))

print('python is top language'.startswith('is', 7, 20))

print('pytahon is top language'.count('a'))

print('pytahon is top language'.count('a', 9))

print('Python y xy abcy'.replace('y', 'x'))

print('Python y xy abcy'.replace('y', 'x', 1))


print('python@gmail.com'.find('gmail'))

print('python@gmail.com'.find('xmail'))

print('python@gmail.com'.index('gmail'))

# print('python@gmail.com'.index('xmail'))

print('www.python.com'.find('.'))

print('www.python.com'.rfind('.'))

print('Hello'.center(50))

print('$ Hello $'.center(50, '*'))

print('*' * 50)


print('Python'.swapcase())

print('Python'.ljust(25, '-'))

print('Python'.rjust(25, '-'))

print('6161'.zfill(8))

print('+6161'.zfill(8))


print('top' in 'pytahon is top language')

print('topx' not in 'pytahon is top language')

word = '123123'

if word.isdigit() == True:
    print("All chars in word are digit!")
else:
    print("Not all chars in word are digit!")


word = '   ThIS Looks BAd '
print(word.strip().lower().replace('bad', 'good'))


print(' email split '.center(50, '*'))

email = 'xyzadf@gmail.com'
indexPos = email.find('@')
print(indexPos)
print(email[:indexPos])
print(email[indexPos + 1:])

amount = '$9,394,000'
print(amount.replace(',', '').replace('$', ''))


name = 'xyz'
age = 20

f_string = f'My name is {name }  age is {age+5}'
print(f_string)

f_string = f'My name is {name!r}  age is {age+5}'
print(f_string)


s1 = 'Apple'

s2 = 'Apple'

s3 = 'apple'

print(s1 == s2)
print(s1.__eq__(s3))
print(s1 == s3)
print(s1.lower() == s3.lower())
