def some_decorator(f):
    def wraps(*args):
        print(f"calling function '{f.__name__}' args {args}")
        return f(args)
    return wraps


@some_decorator
def decocrated_function(x):
    print(f"with arugment '{x}'")


decocrated_function('python')


def greeting():
    return 'Welcome to Python'


def uppercase_decorator(fun):
    def wrapper():
        func = fun()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


wrapper_calling = uppercase_decorator(greeting)
print(wrapper_calling())


@uppercase_decorator
def greeting():
    return 'Welcome to Python'


print(greeting())


def decor(func):
    def inner():
        print("If: before enhancing function")
        func()
        print("If after Enhancing function")
    return inner


def num():
    print("We wil use this function")


inner_func = decor(num)
print(inner_func())

print('Decorator'.center(50, '*'))


def decor(func):
    def inner():
        print("If: before enhancing function")
        func()
        print("If after Enhancing function")
    return inner


@decor
def num():
    print("We wil use this function")


print(num())
