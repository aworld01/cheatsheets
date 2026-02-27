def func(int1, int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply #This will return values in tuple

# t = func(2,3) #t will become tuple
# print(t)

# print(func(2,3))

add, multiply = func(2,3) #You can store returning values in variables.
print(multiply)
print(add)