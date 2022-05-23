'''
This is a Docstrings example.
'''

def func1(a,b):
    '''This is a function which will calculate average of two numbers'''
    average = (a+b)/2
    print(average)
    # return average

print(__doc__) #to access outside Docstrings
print(func1.__doc__) #to access inside Docstrings