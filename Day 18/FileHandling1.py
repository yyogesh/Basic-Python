import os
os.remove('./files/example.txt')


# If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

if os.path.exist('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    os.remove('The file does not exist')
