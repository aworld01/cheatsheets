#def myfun():
#  print('Hello world')
#  myfun()
#myfun()

#def myfun():
#  i=0
#  i+=1
#  print(i,'Hello world')
#  myfun()
#myfun()

#i=0
#def myfun():
#  global i
#  i+=1
#  print(i,'Hello world')
#  myfun()
#myfun()



##to get and set recursion limit
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(50)
print(sys.getrecursionlimit())

i=0
def myfun():
  global i
  i+=1
  print(i,'Hello world')
  myfun()
myfun()