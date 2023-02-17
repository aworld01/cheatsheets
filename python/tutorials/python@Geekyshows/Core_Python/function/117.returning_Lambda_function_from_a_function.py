'''
We can return a lambda function from a function.
'''

def add():
  y = 20
  return (lambda x : x+y)
a = add()
print(a(10))