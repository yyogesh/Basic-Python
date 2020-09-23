# Print the following number pattern using Python range() and for loop.

# 0
# 0 1
# 0 1 2
# 0 1 2 3

for i in range(5):
    for x in range(i):
        print(x, end=' ')
    print()
