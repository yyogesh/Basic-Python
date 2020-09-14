from decimal import Decimal
# input are
a = 2
b = 3
c = 2
print((6 * (a ** 3)) - ((8 * b ** 2) / (4 * c)) + 11)


print(0.1 + 0.2)

print(format(0.1 + 0.2, '.1f'))


from_float = Decimal(0.1)
from_str = Decimal('0.1')
print('from float: {}\nfrom string: {}'.format(from_float, from_str))

my_decimal = Decimal('0.1')
sum_of_decimals = my_decimal + my_decimal + my_decimal
print(sum_of_decimals == Decimal('0.3'))
