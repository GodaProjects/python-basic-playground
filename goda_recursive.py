def recursive_function(num):
    if num <= 1:
        return 1
    else:
        return num * recursive_function(num-1)


print(recursive_function(5))
