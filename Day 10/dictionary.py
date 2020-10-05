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


dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct['key1'])  # value1
print(dct['key4'])  # value4


print(person['first_name'])  # Asabeneh
print(person['country'])    # Finland
# ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'])
print(person['skills'][0])  # JavaScript
print(person['address']['street'])  # Space street
print(person['city'])       # Error


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

person['first_name'] = 'Eyob'
person['age']
# Checking Keys in a Dictionary

# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print('key2' in dct)  # True
print('key5' in dct)  # False


# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

# syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.pop('key1')  # removes key1 item
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
dct.popitem()  # removes the last item
del dct['key2']  # removes key2 item
