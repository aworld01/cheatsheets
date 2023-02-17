"""
A Decorator function is a function that accepts a function as parameter and returns a function.
A decorator takes the result of a function, modifies the result and returns it.
In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
We use @function_name to specify a decorator to be applied on another function.
"""
"""Example-1"""
# def decor(fun):
#     def wrapper():
#         print("IF: Before Enhancing function...")
#         fun()
#         print("IF: After Enhancing function...")
#     return wrapper

# def num():
#     print("We will use this function")
#     print("and will enhance this in decorator")

# result = decor(num)
# result()


"""Example-2"""
# def decor(fun):
#     def wrapper():
#         print("IF: Before Enhancing function...")
#         fun()
#         print("IF: After Enhancing function...")
#     return wrapper

# @decor
# def num():
#     print("We will use this function")
#     print("and will enhance this in decorator")

# num()


"""Example-3"""
# def decor(num):
#     def wrapper():
#         a = num()
#         return a + 20
#     return wrapper

# @decor
# def num():
#     return 10

# print(num())



"""Example-4"""
# def decor2(num):
#     def wrapper():
#         b = num()
#         mult = b * 5
#         return mult
#     return wrapper

# def decor1(num):
#     def wrapper():
#         a = num()
#         add = a + 5
#         return add
#     return wrapper

# def num():
#     return 10
    
# num = decor1(decor2(num))
# print(num())



"""Example-5"""
def decor2(num):
    def wrapper():
        b = num()
        mult = b * 5
        return mult
    return wrapper

def decor1(num):
    def wrapper():
        a = num()
        add = a + 5
        return add
    return wrapper

@decor1
@decor2
def num():
    return 10

print(num())