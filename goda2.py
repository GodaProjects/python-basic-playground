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

# templated strings where escape sequences are not required
templated_string = '''Goda's best friend is "Tanu"'''
print(templated_string)
print(r"Another example's of a template \n")


# Stirng operations
print(len("Goda"))
print("Goda"[0:2])
print("Goda"[1])
print("Goda"[1:])
print("Goda"[1:-1:2])  # Blah
# cant do string[0]="t"
print("Goda".replace("G", "g"))
print("od" in "Goda")
print("od" not in "Goda")
print("Goda".find("G"))
print("            Goda        ".strip())  # Trim
print(" and ".join(["Goda", "Tanu"]))
print("Goda and tanu".split(" and "))
# another example of templated string
yet_another_templated_string1 = yet_another_templated_string2 = "Goda"
print(f"{yet_another_templated_string1} + {yet_another_templated_string2} = {yet_another_templated_string1 + yet_another_templated_string2}")
print("Goda".lower())
print("Goda".upper())
print("AString123".isalnum())
print("AString 123".isalnum())
print("AString123".isalpha())
print("AString".isalpha())
print("1231231".isdigit())

# casting
print(int(4.3))
print(str(5.4))
# a=97 in sequence and 97=a. How is that, i have no clue. Will check later.
print(chr(97))
print(ord('a'))

# Seperator
print(23, 8, 2005, sep="/")

# no new line at the end of print
print("Goda", end="")

# Data formatting
print("\n%04d %s %.2f %c" % (1, "Goda", 1.2233, 'A'))

# math. has millions of functions. Not trying it now.

# Random integer
print(random.randint(1, 100))

# math.inf - infinity
print(math.inf)
# print(10/0)#Not allowed
print(math.inf-10)
print(math.inf+math.inf)
print(math.inf-math.inf)

# Conditional operators - Python defines the scope of the condition by the indentation. So be careful
age = 15
if age == 15:
    print("its Goda")
elif age < 15:
    print("its tanu")
    print("and she loves chocolate")
else:
    print("Its rama")

# Logical operators
name = "Goda"
if age > 14 and name == "Goda":
    print("Goda rules!")
elif age <= 14 or name == "tanu":
    print("Its Tanu")
elif not age <= 15:
    print("Its rama")

# Terenary operators
age = 15 if name == "Goda" else 14
print(age)

# lists
goda_list = ["Goda", "Tanu", "Rama", 1, 3.14, True]
print(goda_list)
goda_list[3] = 2
print(goda_list)
goda_list[3:4] = [2, 1.12]
print(goda_list)
goda_list[3:3] = [2, 3]
print(goda_list)
tanu_list = goda_list+["Chocs"]
print(tanu_list)
# removes only the first instance. And remove("2") will not work since 2 is a int and not a str
goda_list.remove(2)
print(goda_list)
print(goda_list.pop(4))
print(goda_list)

# Muli dimensional array
goda_multi_dim_array = [[0, 1], [2, 3], [4, 5]]
print(goda_multi_dim_array[0][1])

# Check is something exists in an array
print("Goda" in goda_list)
print("Tanu" not in goda_list)
# print(max(goda_list)) will not work since this is a mixed type
# Print every other item - alternate - Have to learn more on this. Did not understand
print(goda_list)
# -1 means end index
print(goda_list[0:-1:2])
# Print including end index
print(goda_list[0:len(goda_list)+1:2])
# Reverse list - a copy is made here, Negative step shows right to left traversal - just like in for loop we do i-- in java
print(goda_list[::-1])
# in place reversing - Void is called "None" here. In place reverse does not return anything
print(goda_list.reverse())
# reverting the reverse = original
goda_list.reverse()
print(goda_list[-1])
print(goda_list[::2])

# While loop
i = 0
while i < len(goda_list):
    print(goda_list[i])
    i += 1

genereated_list = [x**2 for x in range(1, 11) if x % 2 == 0]
print(genereated_list)

function = (x**2 for x in range(1, 11) if x % 2 == 0)

for generator_number in function:
    print("Generator number: ", generator_number)

j = 0
while(j < 10):
    if j % 2 == 0:
        print("even")
    elif(j % 2 != 0):
        print("odd")
    j += 1

# Iterators
list1 = range(1, 11)
iterator = iter(list1)
print(next(iterator))
print(next(iterator))

# Tuple is an immutable list - not trying now. Anything we can do with list can be done with tuple except modifying them.

# Dictionary or key value pairs
friends = {
    "Goda": "Chellam",
    "Tanu": "Kutty"
}
print(friends)
friends1 = dict([
    ("Goda", "Chellam"),
    ("Tanu", "Kutty")
])
print(friends1)
print(friends1["Goda"])
print(friends1.items())

del friends1["Tanu"]
print(friends1.items())
friends1.pop("Goda")
print(friends1.items())

# Key and value printing
for k in friends:
    print(k)
for v in friends.values():
    print(v)

print("%(Goda)s is %(Tanu)s's friend" % friends)

# Set
set1 = set(["Goda", 1])
set2 = {"Tanu", 2, 2}

print(set1)
print(set2)

set3 = set1 | set2
print(set3)
set3.add("Rama")
print(set3)
print(set3.pop())
set3 |= set2
print(set3)
set3 = set3.intersection(set2)
print(set3)
set3 = set1 | set2
set3 = set3.symmetric_difference(set2)
print(set3)

set3 = set3.difference(set2)
print(set3)

# functions
# function 1 - simple


def function1(num1, num2):
    return num1*num2


print(function1(3, 5))

# Function 2 - with data type and returns two values


def function2(num: int, string: str):
    return num, string


print(function2(1, "Goda"))

# function 3 - with initial values


def function3(num: int = 1, string: str = "Goda"):
    return num, string


# Calling function with initial values without passing in any parameters
print(function3())

# function 4 indefinite number of arguments


def function4(*args):
    for arg in args:
        print(arg)


function4(1, 2, 3, 5)

# functions which return a function - anonymous functions - lambdas


def mult_by(num):
    return lambda x: x*num


print(mult_by(10)(5))

# function that uses a lambda


def function_that_uses_lambda(func):
    for num in range(1, 10):
        print(func(num))


function_that_uses_lambda(mult_by(10))

# list of functions
list_of_functions = [lambda x: x**2, lambda x: x**3]

for function in list_of_functions:
    print(function(2))
