import sys
import math
import random
import threading
import time
from functools import reduce

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
