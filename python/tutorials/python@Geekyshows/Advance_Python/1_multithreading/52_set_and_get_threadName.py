'''
current_thread(): This function returns current thread object.

getName(): Every thread has a name by default, to get the name of thread we can use this method.

setName(name): This method is used to set the name of thread.

name Property: This property is used to get or set name of the thread.
'''

"""Exp-1(current_thread)"""
from threading import Thread, current_thread

def disp():
  print('Child Thread object:', current_thread())
t=Thread(target=disp)
t.start()
print('Main Thread', current_thread())


##Exp-2(getName)
#from threading import Thread, current_thread

#def disp():
#  c=current_thread()
#  print('Child Thread object:', c.getName())
#t=Thread(target=disp)
#t.start()
#c=current_thread()
#print('Main Thread:', c.getName())


##Exp-3(setName)
#from threading import Thread, current_thread

#def disp():
#  c=current_thread()
#  print('Child Thread object:', c.getName())
#  c.setName('T-1')
#  print('newNamed Child Thread object:', c.getName())
#t=Thread(target=disp)
#t.start()
#c=current_thread()
#print('Main Thread:', c.getName())
#c.setName('M-1')
#print('newNamed Main Thread:', c.getName())


##Exp-4(name)
#from threading import Thread, current_thread

#def disp():
#  c=current_thread()
#  print('Child Thread object:', c.name)
#t=Thread(target=disp)
#t.start()
#c=current_thread()
#print('Main Thread:', c.name)


##Exp-5(name='new')
#from threading import Thread, current_thread

#def disp():
#  c=current_thread()
#  print('Child Thread object:', c.name)
#  c.name='T-1'
#  print('newNamed Child Thread object:', c.name)
#t=Thread(target=disp)
#t.start()
#c=current_thread()
#print('Main Thread:', c.name)
#c.name='M-1'
#print('newNamed Main Thread:', c.name)


##Exp-6
#from threading import Thread

#def disp():
#  pass
#t=Thread(target=disp)
#print('Default:', t.getName())
#t.setName('T-1')
#print('New:', t.getName())


##Exp-7
#from threading import Thread

#def disp():
#  pass
#t=Thread(target=disp)
#print('Default:', t.name)
#t.name='T-1'
#print('New:', t.name)


##Exp-8
from threading import Thread

def disp():
  pass
t=Thread(target=disp, name='myThread')
print('Default:', t.name)