# Print the following number pattern using Python range() and for loop.

# 1
# 2 2
# 3 3 3

for num in range(4):
    for i in range(num):
        print(num, end=' ')
    print()
