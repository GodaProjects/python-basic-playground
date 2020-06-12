import sys
import math
import random
import threading
import time
from functools import reduce

# Multi line statement with paranthesis
v1 = (
    "Goda " + "and "
    "Tanu"
)
print(v1)

# Multi line statement - not very common
v2 = "Goda " + "and " \
    "Rama"
print(v2)

# Multi statement line
v3 = "Goda"
v4 = " Tanu"
print(v3, v4)

# Type of a value - int
print(type(10))

# max size for int
print(sys.maxsize)

# Max floar value. Floats are accurate upto 15 digits.
print(sys.float_info.max)

# Complex number = real + imaginary number
complex_number = 5 + 6j
print(complex_number)


# math. has millions of functions. Not trying it now.

# Random integer
print(random.randint(1, 100))

# math.inf - infinity
print(math.inf)
# print(10/0)#Not allowed
print(math.inf-10)
print(math.inf+math.inf)
print(math.inf-math.inf)
