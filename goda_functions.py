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
