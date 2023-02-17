'''
Many threads trying to access the same object can lead to problems like making data inconsistent or getting unexpected output, so when a thread is already accessing an object, preventing any other thread accessing the same object is called Thread Synchronization.

The object on which the threads are synchronized is called Synchronized Object or Mutually Exclusive Lock(mutex).

Thread Sunchronization is recommended when multiple threads are acting on the same object simultaneously.

There are following techinques to do Thread Synchronization:
1.Using Locks
2.Using RLock (Re-Entrant Lock)
3.Using Semaphores

A.LOCKS: Locks are typically used to synchronize access to a shared resource. Lock can be used to lock the object in which the thread is acting. A lock has only two states, locked and unlocked. It is created in the unlocked state.


acquire(): This method is used to changes the state to locked and returns immediately. When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked, then the acquire() call resets it to locked and returns.
Syntax:
acquire(blocking=True, timeout=-1) (default)

True: It blocks until the lock is unlocked, then set it to locked and return True.

False: It doesn't block. If a call with blocking set to True would block, return False immediately; otherwise, set the lock to locked and return True.

Timeout: When invoked with the floating-point timeout argument set to positive value, block for at most the number of seconds specified by timeout and as long as the lock can't be acquired. A timeout argument of -1 specifies an unbounded wait. It is forbidden to specify a timeout when blocking is False.

The return value is True if the lock is acquired successfully, False if not (for example if the timeout expired)


release(): This method is used to release a lock. This can be called from any thread, not only the thread which has acquired the lock.

When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.

When invoked on an unlocked lock, a RuntimeError is raised.
There is no return value.
Syntax:
release()
'''

from threading import Thread, current_thread, Lock
class Flight:
    def __init__(self, available_seat):
        self.available_seat=available_seat
        self.l=Lock()
    def reserve(self, need_seat):
        self.l.acquire()
        print('Available Seats:', self.available_seat)
        if(self.available_seat>=need_seat):
            name=current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat-=need_seat
        else:
            print('Sorry! All seats has alloted')
        self.l.release()
f=Flight(2)
t1=Thread(target=f.reserve, args=(1,), name='Rahul')
t2=Thread(target=f.reserve, args=(1,), name='Sonam')
t3=Thread(target=f.reserve, args=(1,), name='Raj')
t1.start()
t2.start()
t3.start()