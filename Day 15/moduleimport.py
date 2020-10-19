# from <module name> import *
import math
from math import sqrt, pow
from cmath import *
from math import *
print("namespace_1: ", dir())

print("namespace_2: ", dir())
print(sqrt(144.2))

print("namespace_3: ", dir())
print(sqrt(144.2))

# namespace_1: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# namespace_2: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
# 12.00833044182246
# namespace_3: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'phase', 'pi', 'polar', 'pow', 'radians', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
# (12.00833044182246+0j)

# we’ve imported two distinct math modules, one after the other. There are some common names which both of these modules have. So, the second module will override the definitions of functions in the first.


# from <module name> import <foo_1>, <foo_2>
print("namespace_1: ", dir())

print("namespace_2: ", dir())
print(sqrt(144.2))

# namespace_1: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# namespace_2: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'pow', 'sqrt']
# 12.00833044182246


# import <module name>
# It is the most reliable and suggested way of importing a module. However, it comes with a catch that you need to prefix the name of the module before using any name from it. But you can prevent the program from polluting the namespace and freely define functions with matching names in the module.

print("namespace_1: ", dir())

print("namespace_2: ", dir())
print(math.sqrt(144.2))

# namespace_1: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# namespace_2: ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math']
# 12.00833044182246
