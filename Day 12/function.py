def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)


generate_full_name()  # calling a function


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)


add_two_numbers()

# Function can also return values, if a function does not return any, the value of the function is None. Lets rewrite the above functions using return. From now on, we get a value when calling the function, instead of printing it.


def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total


print(add_two_numbers())


def greetings(name):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings('Asabeneh'))


def add_ten(num):
    ten = 10
    return num + ten


print(add_ten(90))


def square_number(x):
    return x * x


print(square_number(2))


def print_name(firstname):
    return firstname


print_name('Asabeneh')  # Asabeneh


def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name


print_full_name(firstname='Asabeneh', lastname='Yetayeh')


def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area


print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)


sum_of_numbers(10)  # 55
sum_of_numbers(100)  # 5050


def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print('Full Name: ', generate_full_name('Asabeneh', 'Yetayeh'))


def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum


print('Sum of two numbers: ', sum_two_numbers(1, 9))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print('Age: ', calculate_age(2019, 1819))


def weight_of_object(mass, gravity):
    # the value has to be changed to a string first
    weight = str(mass * gravity) + ' N'
    return weight


print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)


print_fullname(firstname='Asabeneh', lastname='Yetayeh')


def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)


add_two_numbers(num2=3, num1=2)  # Order does not matter


def is_even(n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break
    return False


print(is_even(10))  # True
print(is_even(7))  # False


def greetings(name='Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message


print(greetings())
print(greetings('Asabeneh'))


def generate_full_name(first_name='Asabeneh', last_name='Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())
print(generate_full_name('David', 'Smith'))


def calculate_age(birth_year, current_year=2019):
    age = current_year - birth_year
    return age


print('Age: ', calculate_age(1819))


def weight_of_object(mass, gravity=9.81):
    # the value has to be changed to string first
    weight = str(mass * gravity) + ' N'
    return weight


# 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100))
print('Weight of an object in Newtons: ', weight_of_object(
    100, 1.62))  # gravity on the surface of the Moon


def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num
    return total


print(sum_all_nums(2, 3, 5))


# You can pass functions around as parameters
def square_number(n):
    return n * n


def do_something(f, x):
    return f(x)


print(do_something(square_number, 3))
