def func(a, b):
    """This is function which will calculate average of two numbers."""
    average = (a+b)/2
    return average

v = func(5, 7)
print(v)

print(func.__doc__) #Docstring