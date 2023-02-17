'''
An exception is a runtime error which can be handled by the programmer.
All exceptions are represented as classes in Python.

There are two types of Exception:-
1.Built-in Exception: Exception which are already available in Python Language. The base class for all built-in exceptions is BaseException class.
2.User Defined Exception: A programmer can create  his own exceptions, called user-defined exceptions.

Need of Exception_Handling:-
a.When an exception occurs, the program terminates suddenly.
b.Suddenly termination of program may corrupt the program.
c.Exception may cause data loss from the database or a file.

Try: The try block contains code which may cause exceptions.
Syntax:-
try:
    statements

Except: The except block is used to catch an exception that is raised in the try block. There can be multiple except block for try block.
Syntax:-
except ExceptionName:
    statements

Else: This block will get executed when no exception is raised. Else block is executed after try block.
Syntax:-
else:
    statements

Finally: This block will get executed irrespective of whether there is an exception or not.
Syntax:-
finally:
    statements

Some points for Exception_Handling
a.We can write several except blocks for a single try block.
b.We can write multiple except blocks to handle multiple exceptions.
c.We can write try block without any except blocks.
d.We can't write except block without a try black.
e.Finally block is always executed irrespective of whether there is an exception or not.
f.Else block is optional.
g.Finally block is optional.
'''

'''
##ZeroDivisionError: division by zero
a = 10
b = 0
c = a/b
print(c)
print('Inside Try') #This code also will be not executed
'''
##After Handling
# a = 10
# b = 0
# try:
#     c = a/b
#     print(c)
#     print('Inside Try') #This code also will be not executed
# except ZeroDivisionError:
#     print('Division by Zero is not allowed')
# print('Rest of the code')



'''
##Exception Handling with else block
a = 10
b = 0
try:
    c = a/b
    print(c)
    print('Inside Try')
except ZeroDivisionError:
    print('Division by Zero is not allowed')
else:
    print('Inside Else') #if exception not throw
print('Rest of the code')
'''
##After Handling
# a = 10
# b = 2
# try:
#     c = a/b
#     print(c) #if exception not throw
#     print('Inside Try') #if exception not throw
# except ZeroDivisionError:
#     print('Division by Zero is not allowed')
# else:
#     print('Inside Else') #if exception not throw
# print('Rest of the code')



'''
##Exception Handling with Finally block
a = 10
b = 0
try:
    c = a/b
    print(c)
    print('Inside Try')
except ZeroDivisionError:
    print('Division by Zero is not allowed')
else:
    print('Inside Else') #if exception not throw
finally:
    Print('Inside Finally')
print('Rest of the code')
'''
##After Handling
# a = 10
# b = 2
# try:
#     c = a/b
#     print(c)
#     print('Inside Try')
# except ZeroDivisionError:
#     print('Division by Zero is not allowed')
# else:
#     print('Inside Else') #if exception not throw
# finally:
#     print('Inside Finally')
# print('Rest of the code')



##Exception Handling as object
# a = 10
# b = 0
# try:
#     c = a/b
#     print(c)
#     print('Inside Try')
# except ZeroDivisionError as obj:
#     print(obj)
# print('Rest of the code')



'''
##Exception Handling with NameError
a = 10
b = 2
try:
    c = a/h #this will throw name error
    print(c)
    print('Inside Try')
except ZeroDivisionError:
    print('Division by Zero is not allowed')
else:
    print('Inside Else') #if exception not throw
finally:
    print('Inside Finally')
print('Rest of the code')
'''
##After Handling
# a = 10
# b = 0
# try:
#     c = a/h #this will throw name error
#     print(c)
#     print('Inside Try')
# except NameError as ob:
#     print(ob)
# print('Rest of the code')




##Multiple Exception Handling
# a = 10
# b = 0
# try:
#     c = a/b #this will throw name error
#     print(c)
#     print('Inside Try')
# except (NameError, ZeroDivisionError) as ob: #this will Handle multiple errors.
#     print('Exception Handling')
# print('Rest of the code')




##Multiple Exception Handling
# a = 10
# b = 0
# try:
#     c = a/j
#     print(c)
#     print('Inside Try')
# except (NameError, ZeroDivisionError) as ob: #this will Handle multiple errors.
#     print(ob)
# print('Rest of the code')




##Exception Handling by only except
# a = 10
# b = 0
# try:
#     c = a/b
#     print(c)
#     print('Inside Try')
# except:
#     print('This will Handle any type of exceptions') #This will Handle any type of exceptions
# print('Rest of the code')





#Exception Handling with logic
a = 10
b = 0
try:
    c = a/b
    print(c)
    print('Inside Try')
except:
    print(a/5)
print('Rest of the code')