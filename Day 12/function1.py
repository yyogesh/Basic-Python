# function
# z = f(x, y)

def my_fun():
    print("Hello from my function")


my_fun()
my_fun()
my_fun()


# if __name__ == "__main__":
#     my_fun()


def add():
    print(10 + 5)


add()
add()
print('add() ==> ', add())


def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())


def add():
    return 10 + 5


result = add()
print('Add funciotn reuslt ', result)


def add(x, y):
    return x + y


print(add(10, 20))
print(add(20, 20))
print(add(30, 20))


def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area


print(area_of_circle(10))


def generate_full_name(first_name='Asabeneh', last_name='Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


print(generate_full_name())
print(generate_full_name('David', 'Smith'))


def add(x=1, y=1):
    return x + y


print(add(10, 20))
print(add())


def add(x, y):
    return x + y


print(add(y=20, x=10))


def sum_all_nums(*nums):
    print(nums)
    total = 0
    for num in nums:
        total += num     # same as total = total + num
    return total


print(sum_all_nums(2, 3, 5))
print(sum_all_nums(2, 3, 5, 7, 9))


# def generate_groups(team, *args):
#                  print(team)
#                      for i in args:
#                      print(i)


# generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob')


def fun(a, b, c):
    print(a, b, c)


fun(*[1, 2, 3])


string = 'test'


def test(str):
    str = 'testing'
    print("Inside function : ", str)


test(string)
print("Outside function : ", string)

xList = [10, 20, 30]


def test(iList):
    iList.append(40)
    print("Inside function : ", iList)


test(xList)
print("Outside function : ", xList)


def sum_all_nums(*nums):  # tuples
    print(nums)
    total = 0
    for num in nums:
        total += num     # same as total = total + num
    return total


print(sum_all_nums(2, 3, 5))


def sum_all_nums(**nums):  # kwargs dictionary
    print(nums)
    total = 0
    for num in nums.values():
        total += num     # same as total = total + num
    return total


print(sum_all_nums(a=1, b=2, c=3))


def my_sum(*args):
    result = 0
    for x in args:
        result += x
        return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
print(my_sum(*list1, *list2, *list3))
