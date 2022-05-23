from threading import Thread, current_thread

# def disp():
#     print("This is not a daemon Thread...")

# t = Thread(target=disp)
# print(t.daemon) #to check the thread is deamon or not
# t.start()



"""you can only set thread status(Deamon) before starting thread"""
# def disp():
#     print("This is a daemon Thread...")

# t = Thread(target=disp)
# t.daemon = True #to make daemon thread
# print(t.daemon)
# t.start()



"""MainThread is always non-daemon thread"""
# main = current_thread()
# print(main.name) #to check the name of thread
# print(main.daemon) #to check the thread is  deamon or not



"""
Rest of the threads inherits daemon nature from their parents:
    If parent thread is non-daemon then child thread will become non-daemon thread.
    If parent thread is daemon then child thread will also become a daemon thread.
"""
"""Example-1"""
# main = current_thread()
# print(main.name, main.daemon) #to check thread is deamon or not

# def disp():
#     print("This is a child thread...")
# t = Thread(target=disp) #creating a childThread of MainThread
# print(t.name, t.daemon) #to check thread is deamon or not


"""Example-2"""
# main = current_thread()
# print(main.name, main.daemon) #to check thread is deamon or not

# def disp():
#     thread2 = Thread(target=show)
#     print(thread2.name, thread2.daemon)
# def show():
#     pass
# thread1 = Thread(target=disp)
# print(thread1.name, thread1.daemon) #to check thread is deamon or not
# thread1.daemon = True
# thread1.start()
# print(thread1.name, thread1.daemon) #to check thread is deamon or not



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