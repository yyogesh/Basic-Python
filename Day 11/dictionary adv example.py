import copy

keys = ['Hindi', 'English', 'Math']  # list
new_dic = dict.fromkeys(keys)
print(new_dic)


keys = ['Hindi', 'English', 'Math']  # list
new_dic = dict.fromkeys(keys, 'subject')
print(new_dic)

keys = ['Hindi', 'English', 'Math']  # list
new_dic = {key: 'subject' for key in keys}
print(new_dic)


locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}


exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]


loc = 1

# for direction in exits[loc].keys():
#     print(direction)
# availabelExists = ', '.join(exits[loc].keys())
# print(availabelExists)

# while True:
#     availabelExists = ''
#     availabelExists = ', '.join(exits[loc].keys())
#     print(locations[loc])
#     if loc == 0:
#         break
#     direction = input("Available exist are " + availabelExists + " ").upper()
#     print()
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You can not go in that direction")


d = {1: 'one',  2: 'two'}
d1 = {3: 'three'}
d.update(d1)
d.update(d1)
print(d)

wordsDict = {"Hello": 56, "at": 23, "test": 43,
             "this": 43, "who": [56, 34, 44]}

newDict = wordsDict.copy()

newDict['at'] = 200
print(wordsDict)
print(newDict)

newDict['who'].append(200)
print(wordsDict)
print(newDict)

print('Deep copy'.center(50, '*'))

wordsDict = {"Hello": 56, "at": 23, "test": 43,
             "this": 43, "who": [56, 34, 44]}

newDict = copy.deepcopy(wordsDict)
newDict['who'].append(200)
print(wordsDict)
print(newDict)


wordsDict = {"hello": 56, "at": 23, "test": 43,
             "this": 43, "who": [56, 34, 44]}


for i in sorted(wordsDict.keys()):
    print(i)
