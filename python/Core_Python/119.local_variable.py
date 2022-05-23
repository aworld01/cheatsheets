'''
The variable which are declared inside a function called as local_variabe.
Local_variable scope is limited only to that function where it is created. It means local_variable value is available only in that function not outside of that function.
Ex:-
#def show():
#  x=10 #local_variable
#  print(x)
#show()
print(x)
'''

def show():
  x=10 #local_variable
  print(x)
show()
##print(x) #this will throw error.