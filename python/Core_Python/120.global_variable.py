'''
When a variable is declared above a function, it becomes global_variable.
These variables are available to all the function which are written after it.
The scope of global_variable is the entire program body written below it.
Ex:-
a=50 #global_variable
def show():
  x=20
  print('This is the Local_variable inside the body of function:', x)
  print('This is the Global variable inside the body of function:', a)
show()
print('This is the Global variable out side the body of function', a)
'''

a=50 #global_variable
def show():
  x=20 #local_variable
  print('This is the Local_variable inside the body of function:', x)
  print('This is the Global variable inside the body of function:', a)
show()
print('This is the Global variable out side the body of function:', a)