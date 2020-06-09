# a map is used to run function on a list
def function(x): return x**2


lst = range(1, 10)
resulting_lst = list(map(function, lst))

print(resulting_lst)
