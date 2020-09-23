# Inverted Pyramid pattern with numbers
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

b = 0
for row in range(5, 0, -1):
    b += 1
    for col in range(1, row + 1):
        print(b, end=' ')
    print("")
