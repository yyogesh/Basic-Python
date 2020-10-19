def my_gen():
    n = 1
    print('this is printed first')

    yield n

    n += 1
    print("this is printed sceond")

    yield n
    n += 1
    print("this is printed last statement")
    yield n


for item in my_gen():
    print(item)
