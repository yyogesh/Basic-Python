c = 1  # global variable


# def add():
#     c = c + 2
#     print(c)


# add()

def add():
    global c
    c = c + 2
    print('inside ', c)


print('outside ', c)
add()
