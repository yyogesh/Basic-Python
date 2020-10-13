def greeting(name):
    print('Hello ', name)


greeting('Ravi')


greeting = lambda name: 'Hello ' + name

print(greeting('Ravi'))

def square(num):
    print(num * num)

square(9)

result = (lambda num : num * num)(5)
print(result)

fullName = lambda first, last : f'Full name: {first.title()} {last.title()}'
print(fullName('zy', 'abc'))



high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))


print((lambda x:(x % 2 and 'odd' or 'even'))(3))

(lambda x, y, z: x + y + z)(1, 2, 3)

(lambda x, y, z=3: x + y + z)(1, 2)

(lambda x, y, z=3: x + y + z)(1, y=2)

(lambda *args: sum(args))(1,2,3)

(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)

alist = [lambda m:m**2, lambda m,n:m*n, lambda m:m**4]

print(alist[0](10), alist[1](2, 20), alist[2](3))

aDict = {'m': lambda x:2*x, 'n': lambda x:3*x}

print(aDict['m'](9))