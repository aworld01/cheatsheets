'''
We can create our own thread child class by inheriting Thread Class from threading module.
Syntax:
class childClassName(Thread):
    statements
thread_object=childClassName()

Exp:
class myThread(Thread):
    pass
t=myThread()
'''

# from threading import Thread
##Example-1
# class MyThread(Thread):
#     pass
# t=MyThread()
# print(t.name)


'''
THREAD CLASS'S METHODS
start(): Once a thread is created it should be started by calling start() method.

run(): Every thread will run this method when thread is started. We can override this method and write our own code as body of the method. A thread will terminate automatically when it comes out of the run() method.

join(): This method is used to wait till the thread completely executes the run() method.
'''

##Example-1
# from threading import Thread
# class MyThread(Thread):
#     def run(self):
#         print('Run method')
# t=MyThread()
# t.start()


##Example-2
from threading import Thread
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print('Child Thread')
t=MyThread()
t.start()
t.join() #to run Child Thread at first
for i in range(5):
    print('Main Thread')