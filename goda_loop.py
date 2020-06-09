# While loop
goda_list = ["Goda", "Tanu", "Rama", 1, 3.14, True]
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
