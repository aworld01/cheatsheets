'''
This is one of the oldest synchronization primitives in the history of computer science, invented by the early Dutch computer scientist Edsger W. Dijkstra.

A semaphore manages an internal counter which is decremented by each acquire() call and incremented by each release() call.

The counter can never go below zero; when acquire() finds that it is zero, it blocks, waiting until some other thread calls release().

It's usually better to use the BoundedSemaphore class, which considers it to be an error to call release more often than you've called acquire.

01:00/16:21
'''
##with Semaphore(2)
# from threading import Thread, current_thread, Semaphore
# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat=available_seat
#         self.l=Semaphore(2) #to thread will lock this one.
#         print(self.l)
#         print(self.l._value)
#     def reserve(self, need_seat):
#         self.l.acquire()
#         print('Available Seats:', self.available_seat)
#         if(self.available_seat>=need_seat):
#             name=current_thread().name
#             print(f'{need_seat} seat is alloted for {name}')
#             self.available_seat-=need_seat
#         else:
#             print('Sorry! All seats has alloted')
#         self.l.release()
# f=Flight(2)
# t1=Thread(target=f.reserve, args=(1,), name='Rahul')
# t2=Thread(target=f.reserve, args=(1,), name='Sonam')
# t3=Thread(target=f.reserve, args=(1,), name='Raj')
# t1.start()
# t2.start()
# t3.start()



##with BoundedSemaphore(2)
from threading import Thread, current_thread, BoundedSemaphore
class Flight:
    def __init__(self, available_seat):
        self.available_seat=available_seat
        self.l=BoundedSemaphore(2) #to thread will lock this one.
        print(self.l)
        print(self.l._value)
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