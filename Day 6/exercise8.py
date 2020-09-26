# Print the following number pattern using Python range() and for loop.

# 0
# 0 1
# 0 1 2
# 0 1 2 3

# for i in range(5):
#     for x in range(i):
#         print(x, end=' ')
#     print()


for i in range(5):
    print(i)


for i in range(5):
    print('Value of i ==> : ', i)
    # print('2nd loop start'.center(50, '*'))
    for x in range(i):
        print('value of x : ', x)
    print('Upper loop end')

for i in range(5):
    for x in range(i):
        print(x, end=' ')
    print()

# 0
# 0 1
# 0 1 2
# 0 1 2 3

for row in range(5, 0, -1):
    print(row)
