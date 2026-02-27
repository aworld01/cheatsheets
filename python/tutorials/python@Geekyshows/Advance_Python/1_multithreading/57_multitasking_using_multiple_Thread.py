'''
When multiple tasks are executed at a time, then it is called Multi-tasking. For this purpose we need more than one Thread and when we use more than one Thread. It is called Multi-Threading.
'''

##two Task using two Thread
from threading import Thread
from time import sleep

class Hotel:
    def __init__(self, t):
        self.t=t

    def food(self):
        for i in range(1, 6):
            print(self.t, i)
            sleep(2)
h1=Hotel('Take order from table No.')

h2=Hotel('Serve order to table No.')
t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
t2.start()