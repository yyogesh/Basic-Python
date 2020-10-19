def outer():
    x = 'local'

    def inner():
        nonlocal x

    x = "nonLocal"
    print('inner: x', x)
    inner()
    print("outer : x ", x)


outer()
