'''
Thread class of threading module is used to create threads. To create our own thread we need to create an object of Thread Class.

FOLLOWING ARE THE WAYS OF CREATING THREADS:-
1.Creating a thread without using a class
2.Creating a thread by creating a child class to Thread class
3.Creating a thread without creating child class to Thread class

We can create an independent thread child class that does not inherit from Thread Class from threading module.
Syntax:
class ClassName():
    statements
object_name=ClassName()

Thread_object=Thread(target=object_name.function_name, args=(arg1, arg2, ...))

Exp:
class MyThread:
    def disp(self, a, b):
        print(a, b)
myT=MyThread()
t=Thread(target=myT.disp, args=(10, 20))
t.start()
'''

from threading import Thread
class MyThread:
    def disp(self, a, b):
        print(a, b)
myT=MyThread()
t=Thread(target=myT.disp, args=(10, 20))
t.start()