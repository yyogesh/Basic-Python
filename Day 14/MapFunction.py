import functools

items = [1, 2, 3, 4, 5]

square = []


def mapfun(x):
    return x ** 2


square = list(map(mapfun, items))
print(square)

squared = list(map(lambda x: x ** 2, items))
print(squared)


def multiply(x):
    return (x*x)


def add(x):
    return (x+x)


func = [multiply, add]

for i in range(5):
    value = list(map(lambda x: x(i), func))
    print(value)


scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]


def studentMarks(score):
    return score > 75


over_75 = list(filter(studentMarks, scores))
print(over_75)


dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)


list = [1, 2, 3, 4]
result = functools.reduce(lambda a, b: a + b, list)
print(result)
