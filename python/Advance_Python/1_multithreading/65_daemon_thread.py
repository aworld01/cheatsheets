"""
A deamon thread is a thread which runs continuously in the background.
It provides support to nun-daemon threads.
When last non-daemon thread terminates, automatically all daemon threads will be terminated. We are not required to terminate daemon thread explicitly.

CREATE DAEMON THREAD
setDaemon(True) method or daemon = True property is used to make a thread a daemon thread.
Example:-
    t1 = Thread(target=disp)
    t1.setDaemon(True) / t1.daemon = True

setDaemon(True / False): This method is used to set a thread as daemon thread.
You can set thread as daemon only before starting that thread which means active thread status can't be changed as daemon.
If we pass True non-daemon thread will become daemon and if False daemon thread will become non-daemon.

daemon Property: This property is used to check whether a thread is daemon or not. It returns True if thread is daemon else False.
We can also use daemon property to set a thread as daemon thread or vice versa.

isDaemon(): This method is used to check whether a thread is daemon or not. It returns True if thread is daemon else False.
"""
from threading import Thread, current_thread

"""example-1"""
# def disp():
#     print("This is not a daemon Thread")

# t = Thread(target=disp)
# print(t.isDaemon()) #to check thread is deamon or not



"""example-2"""
"""you can only set thread status(Deamon) before starting thread"""
# def disp():
#     print("This is a daemon Thread")

# t = Thread(target=disp)
# print("Before making Daemon:",t.isDaemon()) #to check thread is deamon or not
# t.setDaemon(True) #to make daemon
# print("After making Daemon:",t.isDaemon())



"""example-3"""
# def disp():
#     print("This is not a daemon Thread")

# t = Thread(target=disp)
# print(t.daemon) #to check thread is deamon or not



"""example-4"""
# def disp():
#     print("This is a daemon Thread")

# t = Thread(target=disp)
# print("Before making Daemon:",t.isDaemon()) #to check thread is deamon or not
# t.daemon = True #to make daemon
# print("After making Daemon:",t.isDaemon())



"""MainThread is always non-daemon thread"""
# from threading import current_thread
# main = current_thread()
# print(main.getName()) #to check current thread name
# print(main.daemon) #to check thread is deamon or not



"""
Rest of the threads inherits daemon nature from their parents:
    If parent thread is non-daemon then child thread will become non-daemon thread.
    If parent thread is daemon then child thread will also become a daemon thread.
"""
"""example-1"""
# from threading import current_thread
# main = current_thread()
# print(main.getName(), main.daemon)  #to check thread is deamon or not
# """making a function"""
# def disp():
#     print("Disp function...")
# """making a thread"""
# thread1 = Thread(target=disp) #creating ChildThread of MainThread
# print(thread1.getName(), thread1.daemon)  #to check thread is deamon or not


"""example-2"""
# from threading import current_thread
# main = current_thread()
# print(main.getName(), main.daemon)  #to check thread is deamon or not
# """making a function"""
# def disp():
#     """creating a ChildThread"""
#     thread2 = Thread(target=show)
#     print(thread2.getName(), thread2.daemon)  #to check thread is deamon or not
# def show():
#     pass
# """creating a thread"""
# thread1 = Thread(target=disp) #creating ChildThread of MainThread
# print(thread1.getName(), thread1.daemon) #to check thread is deamon or not
# thread1.daemon = True #to creating a daemon thread
# print(thread1.getName(), thread1.daemon) #to check thread is deamon or not
# thread1.start() #to starting the thread
# thread1.join() #to wait till child thread stop executing


"""
When last non-daemon thread terminates, automatically all daemon threads will be terminated. We are not required to terminate daemon thread explicitly.
"""
from threading import Thread, current_thread
from time import sleep

"""creating a function"""
def teacher():
    for i in range(1, 11):
        print("Teaching Session", i)
        sleep(1)
"""creating a thread"""
t1 = Thread(target=teacher)
t1.daemon = True #to make daemon thread
t1.start()
sleep(6)
print("Exam finished...")