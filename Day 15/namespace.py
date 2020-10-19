a_var = 10
print("begin()-> ", dir())


def foo():
    b_var = 11
    print("inside foo()-> ", dir())


foo()

print("end()-> ", dir())


# begin()->  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a_var']
# inside foo()->  ['b_var']
# end()->  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a_var', 'foo']
