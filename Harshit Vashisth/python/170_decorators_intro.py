"""Decorators: enhance the functionality of other functions"""


"""example-1"""
# def func1():
#     print("This is function-1")

# def func2():
#     print("This is function-2")
    
# def decorator_function(any_func):
#     def wrapper():
#         print("This is awesome function...")
#         any_func()
#         print()
#     return wrapper

# var = decorator_function(func1)
# var()



"""example-2"""
def decorator_function(any_func):
    def wrapper():
        print("This is awesome function...")
        any_func()
        print()
    return wrapper

@decorator_function
def func1():
    print("This is function-1")

@decorator_function
def func2():
    print("This is function-2")

func1()
func2()