'''
Two or more thread cummunicate with each other that is known as Thread communication.

There are three ways of Thread communication:-
1.Event
2.Condition
3.Queue

Event: This is one of the simplest mechanisms for cummunication between threads:
One thread signals an event and other threads wait for it.

An event object manages an internal flag that can be set true with the set() method and reset to false with the clear() method. The wait() method blocks until the flag is true.
The flag is initially false.
Syntax:
from threading import Event
e=Event()

set(): It sets the internal flag to true. All threads waiting for it to become true are awakened. Threads that call wait() once the flag is true will not block at all.

clear(): It sets the internal flag to False. Subsequently, threads calling wait() will block until set() is called to set the internal flag to true again.

is_set(): It returns true if and only if the internal flag is true.

wait(timeout=None): It blocks until the internal flag is true. If the internal flag is true on entry, return immediately. Otherwise, block until another thread calls set() to set the flag to true, or until the optional timeout occurs.
When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof).
This method returns true if and only if the internal flag has been set to true, either before the wait call or after the wait starts, so it will always return True except if a timeout is given and the operation times out.
'''

from threading import Thread, Event
from time import sleep

e=Event()
def light_switch():
    sleep(2)
    e.set()
    print('Geen light is ON:')
    sleep(4)
    print('Red light is ON:')
    e.clear()
def traffic():
    e.wait()
    if e.is_set():
        print('You can Go.......')
t1=Thread(target=light_switch)
t2=Thread(target=traffic)
t1.start()
t2.start()