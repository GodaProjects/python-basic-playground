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
