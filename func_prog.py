# functional programming

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))
#################################################################################
# pure function

def polynomial(x):
    return x**2 + 5 * x + 4
print(polynomial(-4))
#################################################################################
print((lambda x: x**2 + 5 * x + 4)(-4)) # use lambda function

double = lambda x: x * 2 # assined lambda function to variale

print(double(7))
##################################################################################
# built-in function map

def add_five(x):
    return x + 5

nums = [11,22,33,44,55]
result = list(map(add_five, nums))
print(result)

