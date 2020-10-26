# if a < 5

# 1 / 0
# try:
# 	You do your operations here;
# 	......................
# except ExceptionI:
# 	If there is ExceptionI, then execute this block.
# except ExceptionII:
# 	If there is ExceptionII, then execute this block.
# 	......................
# else:
# 	If there is no exception then execute this block.


try:
    You do your operations here
    ......................
except ExceptionI:
    If there is ExceptionI, then execute this block.
except ExceptionII:
    If there is ExceptionII, then execute this block.
    ......................
else:
    If there is no exception then execute this block.


print('exception handling'.center(50, '*'))
try:
    print(10 + '5')
except:
    print('Something went wrong')


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2020 - year_born

    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')


try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2020 - year_born

    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type Error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('Zero diviosn error occured')

else:
    print('I usually run with the try block')
finally:
    print('I always run.')
