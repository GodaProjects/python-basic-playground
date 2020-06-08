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
print (v1)

#Multi line statement - not very common
v2 = "Goda " + "and " \
    "Rama"
print (v2)

#Multi statement line
v3="Goda"; v4=" Tanu"
print (v3, v4)

# Type of a value - int
print (type(10))

#max size for int
print (sys.maxsize)

#Max floar value. Floats are accurate upto 15 digits.
print (sys.float_info.max)

# Complex number = real + imaginary number
complex_number = 5 + 6j
print (complex_number)

# templated strings where escape sequences are not required
templated_string = '''Goda's best friend is "Tanu"'''
print(templated_string)
print(r"Another example's of a template \n")


#Stirng operations
print(len("Goda"))
print("Goda"[0:2])
print("Goda"[1])
print("Goda"[1:])
print("Goda"[1:-1:2]) #Blah
# cant do string[0]="t"
print ("Goda".replace("G", "g"))
print ("od" in "Goda")
print ("od" not in "Goda")
print ("Goda".find("G"))
print ("            Goda        ".strip()) # Trim
print (" and ".join(["Goda","Tanu"]))
print ("Goda and tanu".split(" and "))
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

#casting
print (int(4.3))
print (str(5.4))
print (chr(97)) # a=97 in sequence and 97=a. How is that, i have no clue. Will check later.
print (ord('a'))

#Seperator
print (23,8, 2005, sep="/")

# no new line at the end of print
print ("Goda", end="")

# Data formatting
print ("\n%04d %s %.2f %c" %(1, "Goda", 1.2233, 'A'))

#math. has millions of functions. Not trying it now.

# Random integer
print(random.randint(1,100))

# math.inf - infinity
print(math.inf)
#print(10/0)#Not allowed
print(math.inf-10)
print(math.inf+math.inf)
print(math.inf-math.inf)

#Conditional operators - Python defines the scope of the condition by the indentation. So be careful
age=15
if age == 15:
    print ("its Goda")
elif age < 15:
    print("its tanu")
    print("and she loves chocolate")
else:
    print("Its rama")

#Logical operators
name="Goda"
if age >14 and name=="Goda":
    print("Goda rules!")
elif age<=14 or name=="tanu":
    print("Its Tanu")
elif not age <=15:
    print("Its rama")

#Terenary operators
age=15 if name=="Goda" else 14
print (age)