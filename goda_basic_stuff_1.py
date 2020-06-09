import os
from math import sqrt, ceil
import math
print("Hello from Goda!")

# Input from command line
#name = input('Please enter your name: ')
#print (name)

godaMsg = "Hello from Goda!"
print(godaMsg)

x = 5
print(x)

# Array
array = [1, 2, 3, "Goda"]
print(array)
array.append("Tanu")
print(array.index("Goda"))
print("Modified array", array)
print(array[2])
print(array[0:2])
print(array[3:])
array.insert(3, "Rama")
print("Modified array", array)
del array[2]

# Tuple is immutable
tup = ("Rama", "Goda", "Tanu")
print(tup)
print(tup)

# Swapping variables
x = 3
y = 5
x, y = y, x
print(x, y)

# Dictionary - like hashmap
dictionary = {"one": "Rama", "two": "Goda", "three": "Tanu"}
print(dictionary)
print(dictionary["one"])
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# Also seems to be returning something like method references
print(dictionary.items)

# Numbers
print(1+2)
print(2**4)
print(str(2**4) + " Goda")
print(8.0)

# Boolean
boolean = True
print(boolean)

# String
""" This is the block comment
in python. Used in documentation
"""
stringWithNewLine = "Goda\nTanu"
print(stringWithNewLine[2])
print(stringWithNewLine[-2])  # from backward
print(len(stringWithNewLine))
# without str() it will not work. Does not mix string and number
print("Number of characters "+str(len(stringWithNewLine)))
print("Split string is ", "Rama, Goda, Tanu".split(","))

# Functions
# Variables are locally scoped


def add(x, y):
    return x+y


print(add(10, 10))
# global variable in functions, function also takes list as input


def globalVariableCheck():
    global array
    print("Array is ", array)
    for item in array:
        print("Printing item in for loop ", item)


globalVariableCheck()
# returning multiple values


def returnMultipleValues():
    return 1, 3, 4


# same number of variables on LHS as the return from a function
x, y, z = returnMultipleValues()
print("returnMultipleValues ", x, y, z)


def numberOfInputsUnknown(*numbers):
    print(numbers)


numberOfInputsUnknown(1, 2, 3, 4, 5)

# modules
print(math.sin(1))
print(math.ceil(1.10))
# Getting function directly
print(sqrt(4))
print(ceil(1.10))
# all modules of a function
print(dir(math))
print(os.times())

# input from console
# x = input("x: ")
# y = input("y: ")
# print (float(x) + int(y))
