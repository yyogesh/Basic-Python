t = 'a', 'b', 'c'

print(t)


t2 = ('a', 'b', 'c')

print(t)

t1 = (('a', 'b', 'c'))

print(t1 + t2)

t3 = (t1 + t2)

# list = ['test'] * 3

# print(list)

x = ('test') * 3

print(x)

x = ('test', ) * 3

print(x)


print(t1[1])
# immutable
# t1[1] = 'z'


a = b = c = 12
print(c, a)

a, b = 12, 13
print(a, b)

t2 = 'a', 'b', 'c'


a1, b1, c1 = t2

print(a1, b1, c1)

emp_records = ('john', 'hr', 2010, 'robert',
               'account', 2015, 'bill', 'mis', 2018)
(emp_name, emp_dept, emp_join_date) = emp_records[0:3]
print(emp_name)
print(emp_dept)
print(emp_join_date)

weekdays = ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun')
print(weekdays[1:])
print(weekdays[1:5])
print(weekdays[5:1])
print(weekdays[5:])
print(weekdays[:5])
print(weekdays[:-5])
print(weekdays[::-1])

print(len(weekdays))

# list = [1, 2, 3]

# print(tuple(list))

print(tuple('python'))

print(type(weekdays))


py_tuple = (22, 33, 55, 66, [88, 99])
py_tuple[4][0] = 77
py_tuple[4][1] = 88

print(py_tuple)
new_list = list(weekdays)
print(new_list)


imelda = "More Mayhem", "Imelda May", 2011, ((
    1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))


print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

for song in tracks:
    track, title = song
    print('Track number {}, Title : {}'.format(track, title))


imelda = "More Mayhem", "Imelda May", 2011, ([
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])

imelda[3].append((5, "All For You"))
title, artist, year, tracks = imelda

print(title)
print(artist)
print(year)
print(tracks)

tracks.append((6, "Eternity"))
print(tracks)


py_tuple = ('p', 'y', 't', 'h', 'o', 'n')
print('p' in py_tuple)


for index, item in enumerate(py_tuple):
    print(index, item)


tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)

print(tuple1 == tuple2)
print(tuple1 < tuple2)


months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun',
          'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

enumx = enumerate(months, 100)

print(list(enumx))

for index, item in enumerate(months):
    if(index % 2 == 0):
        print(index, item)


cList = [item for index, item in enumerate(months) if index % 2 == 0]
print(cList)
