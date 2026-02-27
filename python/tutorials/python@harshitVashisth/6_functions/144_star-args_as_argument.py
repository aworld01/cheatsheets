def multiply_nums(*args):
    multiply = 1
    for num in args:
        multiply *= num
    return multiply

# nums = [2,3,4]
nums = (2,3,4)
print(multiply_nums(*nums)) #to unpack list/tuple