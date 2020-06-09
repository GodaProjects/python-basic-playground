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
