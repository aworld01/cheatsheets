"""example-1"""
# def multiply_nums(*args):
#     multiply = 1
#     for num in args:
#         multiply *= num
#     return multiply
# print(multiply_nums(1,2,3,4))


"""example-2"""
"""always normal parameter should be at first"""
# def multiply_nums(num, *args):
#     print(num)
#     print(args)
# multiply_nums(2,3,4) #2 will treat like normal parameter


"""example-2 (*args with empty arguments)"""
def multiply_nums(*args):
    print(args) #this will print an empty tuple
multiply_nums()