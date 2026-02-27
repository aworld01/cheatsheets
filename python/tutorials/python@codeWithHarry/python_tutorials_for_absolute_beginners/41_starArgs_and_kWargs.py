'''
normalArguments, arg, kwargs
'''
"""ARGS (works with list and tuple)"""
l = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam"] #list
t = ("Harry", "Rohan", "Skillf", "Hammad", "Shivam") #tuple
# print(l, type(l))
# print(t, type(t))

'''example1'''
# def func(*args):
#     print(args, type(args)) #this will return tuple

# func("Harry", "Rohan", "Skillf", "Hammad", "Shivam")


'''example2'''
def funcArgs(*args):
    print(args, type(args)) #this will return tuple

# funcArgs(l)
# funcArgs(t)
# funcArgs(*l) #to unpack list
# funcArgs(*t) #to unpack tuple



"""KWARGS (works with dictionary)"""
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor", "The Programmer": "Coordinator", "Abdul Zoha": "Programmer"}

"""example1"""
def funcKwargs(**kwargs):
    print(kwargs, type(kwargs))

funcKwargs(**kw)




"""example2"""
def funcKwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

funcKwargs(**kw)