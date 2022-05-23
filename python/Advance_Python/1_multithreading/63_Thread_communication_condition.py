'''
Condition class is used to improve speed of communication between Threads.

The condition class object is called condition variable.

A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. Passing one in is useful when several condition variables must share the same lock. The lock is part of the condition object: you don't have to track it separately.

A condition is a more advanced version of the event object.

CREATE CONDITION OBJECT
from threading import Condition
cv=Condition()

CONDITION METHOD
notify(n=1): This method is used to immediately wake up one threads waiting on the condition.

notify_all(): This method is used to wake up all threads waiting on the condition.

wait(timeout=None): This method wait until notified or until a timeout occurs. If the calling thread has not acquired the lock when this method is called, a RuntimeError is raised. Wait terminates when invokes notify() method or notify_all() method. The return value is True unless a given timeout expired, in which case it is False.
'''

from threading import Thread, Condition
from time import sleep

lst=[]
def produce():
    cv.acquire()
    for i in range(1,6):
        lst.append(i)
        sleep(1)
        print('Item Produced...')
    cv.notify()
    cv.release()
def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print(lst)
cv=Condition()
t1=Thread(target=produce)
t2=Thread(target=consume)

t1.start()
t2.start()
