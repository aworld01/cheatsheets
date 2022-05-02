'''We can pass lambda function to another function.
'''

def show(a):
  print(a)
show(8) #calling the function

def disp(a):
  print(a(20))
disp(lambda x : x) #calling the function