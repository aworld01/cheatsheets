'''
A function without a name is called as Anonymous function. It's also known as Lambda function.
Anonymous function are not defined using def keyword rather they are defined using lambda keyword.
Syntax:-
lambda argument_list : expression
Ex:-
lambda x : print(x)
lambda x, y : x+y

CALLING A LAMBDA FUNCTION
add = lambda x,y : x+y
add(5,2) #calling the function

Lambda function doesn't have any name.
Ex:-

Lambda function returns a function.
Ex:-
show = lambda x : print(x)

Lambda function can take zero or any number of argument but contains only one expression.
Ex:-
lambda x,y : x+y

In lambda function there is no need to write return statement.
It can only contain expressions and can't include statements in its body.
You can use all the type of Actual Arguments.
'''

##EXAMPLE-1 (Normal function)
# def show(x):
#     print(x)
# show('hello') #calling a function

# s = lambda x : print(x)
# s("Hello") #calling a function


##EXAMPLE-2 (Normal function)
# def add(x,y):
#     return x+y
# print(add(2,5)) #calling a function

# add = lambda x,y : x+y
# print(add(7,4)) #calling a function





##RETURN MULTIPLE VALUES
##EXAMPLE-1 (Normal function)
# def show(x,y):
#     add = x+y
#     sub = x-y
#     return add, sub
# add, sub = show(8,4)
# print(add)
# print(sub)

# add_sub = lambda x,y : (x+y, x-y)
# add, sub = add_sub(7,4) #calling a function
# print(add)
# print(sub)





##DEFAULT ARGUMENTS
##EXAMPLE-1 (Normal function)
def add(x,y=5):
    return x+y
print(add(7))

add = lambda x,y=6 : x+y
print(add(10)) #calling a function