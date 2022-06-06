"""example-1"""
# def decorator_function(any_func):
#     def wrapper(*args, **kwargs):
#         print("This is awesome function...")
#         any_func(*args, **kwargs)
#         print()
#     return wrapper

# @decorator_function
# def func(a):
#     print(f"This is function with argument {a}...")

# func(10)



"""example-2"""
def decorator_function(any_func):
    def wrapper(*args, **kwargs):
        print("This is awesome function...")
        return any_func(*args, **kwargs)
        print()
    return wrapper

@decorator_function
def func(a):
    print(f"This is function with argument {a}")

@decorator_function
def add(a,b):
    return a+b

print(add(5,3))
func(6)