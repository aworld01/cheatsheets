'''
If local variable and global variable has same name then the function by default refers to the local variable and ignores the global variable.
It means global variable is not accessible inside the function but possible to access outside of function.
In this situation, if we need to access global variable inside the function we can access it using global keyword followed by variable name.
'''

# a=50 #global variable
# def show():
#     a=10 #local variable
#     print('Local:', a)
# show()
# print('Global:', a)


i=0
def show():
    global i #to access global variable
    while i<5:
        i= i+1
        print('Local:',i)
show()
print('Global:', i)