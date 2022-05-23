'''
This function returns a table of current global variables in the form of dictionary.
'''
a=50
def show():
    a=10
    print('Local variable A:',a)
    x=globals()['a'] #to access local variable and/global variables in a function.
    print('Global variable in function:',x)
    x=40
    print('Modified x value:',x)
show()
print('Global varialbe:',a)