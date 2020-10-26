try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2020 - year_born

    print(f'You are {name}. And your age is {age}.')
except TypeError as err:
    print(err)
    print('Type Error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('Zero diviosn error occured')

else:
    print('I usually run with the try block')
finally:
    print('I always run.')
