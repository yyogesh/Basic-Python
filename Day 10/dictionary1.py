my_dict = {}
# touple = ()

# list = []

print(my_dict)
user = {'name': 'xyz', 'age': 20, 2: 'xy'}

print(user)

my_dict = dict({1: 'apple', 2: 'ball'})


print(my_dict)

print(user.get('name'))

print(len(user))

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(len(person))

print(person['first_name'])
print(person['skills'][2])

print(person['address']['street'])


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"
         }

fruit['lemon'] = "great with tequila"


# while True:
#     dict_key = input("Please enter a fruit: ")
#     if(dict_key == 'quit'):
#         break
#     description = fruit.get(dict_key)
#     print(description)

print(fruit.values())
print(fruit.items())

keys = {'a', 'e', 'i', 'o', 'u'}  # set
vowels = dict.fromkeys(keys)
print(vowels)


keys = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys, 'xyz')
print(vowels)

keys = {'a', 'e', 'i', 'o', 'u'}
vowels = dict.fromkeys(keys, ['English', 'Hindi'])
print(vowels)


vowels = dict.fromkeys(['English', 'Hindi'], 'xyz')
print(vowels)


fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"
         }

print('Loop'.center(50, '*'))
print(fruit.items())

for snack in fruit.items():
    item, description = snack
    print(item + ' is ' + description)
