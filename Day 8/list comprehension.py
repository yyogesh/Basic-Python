# [stmt for var in iterable if predicate]


theList = [iter for iter in range(5)]
print(theList)


listofCountries = ["India", "America",
                   "England", "Germany", "Brazil", "Vietnam"]

firstLetters = [country[0] for country in listofCountries]
print(firstLetters)


numbs = [1, 2, 3, 4, 5]
result = []

for x in numbs:
    if x > 3:
        y = x * x
        result.append(y)

print(result)


result = [x * x for x in numbs if x > 3]
print(result)


result = [x + y for x in 'get' for y in 'set']
print(result)

result = []
for x in 'get':
    for y in 'set':
        result.append(x + y)

print(result)


result = [x + y for x in 'get' for y in 'set' if x != 't' and y != 'e']
print(result)


months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']


enumx = enumerate(months, 100)
print(list(enumx))


for item in enumerate(months):
    print(item)

for count, item in enumerate(months):
    print(count, item)


print([iter for index, iter in enumerate(months) if index % 2 == 0])


langs = ['python', 'csharp', 'go', 'javascript', 'php', 'mysql']
langs = [item.upper() for item in langs]
print(langs)

fruits = ['Apples', 'Oranges', 'Guavas',
          'Grapes', 'Mangoes', 'Apricots', 'Olives']

print([fruit for fruit in fruits if fruit[0] in ['A', 'E', 'I', 'O', 'U']])


"""
 Desc: Program to filter even numbers from a list of 1000 integers
 Method: By using Python list comprehension
"""


list_of_ints = range(1, 1000)


def test_listComprehension():
    list_of_even_nums = [x for x in list_of_ints if x % 2 == 0]
    return list_of_even_nums


out = test_listComprehension()
print([x for x in list_of_ints if x % 2 == 0])

oddNum = []
evenNums = []

evenNums = [x for x in list_of_ints if x % 2 == 0 or oddNum.append(x)]
print(len(evenNums), len(oddNum))
