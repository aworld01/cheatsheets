"""Local_variabe can't be access outside of the function"""
# def func():
#     x=7 # Local_variable
#     return x
# print(func())



"""Global_variable can be access from anywhere"""
# x=5 # Global_variable
# def func1():
#     x=7 # Local_variable
#     return x
# print(func1())
# print(x)


"""access Globle_variable in function"""
# x=5 # Global_variable
# def func1():
#     return x
# print(func1())



"""change Globle_variable value"""
x=5 # Global_variable
def func1():
    x=7 # Local_variable
    return x
print(func1())
print(x)

print()
x=5 # Global_variable
def func1():
    global x # to change value
    x=7
    return x
print(func1())
print(x)