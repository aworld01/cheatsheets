"""kwargs (keyword arguments)"""
"""example-1"""
# def func(**kwargs):
#     print(kwargs, type(kwargs)) #This will get arguments as a dictionary

# func(name = "Abdul Zoha", age = 29)


"""example-2"""
# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k} = {v}")

# func(name = "Abdul Zoha", age = 29)


"""example-3"""
# def func(x, **kwargs):
#     print(x)
#     for k, v in kwargs.items():
#         print(f"{k} = {v}")

# func("Abdul", name = "Abdul Zoha", age = 29)


"""dictionary unpacking"""
def func(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} = {v}")

d = {"name": "Abdul Zoha", "age": 30, "vill":"Chandpali"}
func(**d)