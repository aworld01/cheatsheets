'''
Thread class of threading module is used to create threads. To create our own thread we need to create an object of Thread Class.

Following are the ways of creating threads:-
1.Creating a thread without using a class.
2.Creating a thread by creating a child class to Thread class.
3.Creating a thread without creating child class to Thread class.


thread_object: It represents our thread.
target: It represents the function on which the thread will act.
args: It represents a tuple of arguments which are passed to the function.

t.start(): Once a thread is created it should be started by calling start() method.
'''
"""Thread without arguments"""
# from threading import Thread
# def disp():
#     print('Thread Running...')
# t=Thread(target=disp)
# t.start() #starting a Thread

"""Thread with arguments"""
# from threading import Thread
# def disp(arg):
#     print('Thread Running:', arg)
# t=Thread(target=disp, args=(10,)) #Thread with arguments
# t.start()

"""Thread with MainThread"""
from threading import Thread
from time import sleep
def disp():
    for i in range(5):
        print(i,"Thread-1 Running")
        sleep(2)
t=Thread(target=disp)

def main():
    for i in range(5):
        print(i, "MainThread is running")
        sleep(2)
t.start()
main()