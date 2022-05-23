'''
The Queue class of queue module is useful to create a queue that holds the data produced by the producer.

The data can be taken from the queue and utilized by the consumer.

We need not use locks since queues are thread safe.

Syntax:
from queue import Queue
q=Queue

put(): This method is used by Producer to insert items into the queue.
Syntax:
queue_object.put(item)
Ex:
q.put(i)

get(): This method is used by Consumer to retrieve items from the queue.
Syntax:
producer_object.queue_object.get(item)
Ex:
p.g.get(i)

empty(): This method returns True if queue is Empty else returns False.
Ex:
q.empty()

full(): This method returns True is queue is Full else returns False.
Ex:
q.full()
'''

from threading import Thread
from queue import Queue
from time import sleep

class Producer:
    def __init__(self):
        self.q = Queue()
    def produce(self):
        for i in range(1,6):
            print('Item Produced', i)
            self.q.put(i)
            sleep(1)

class Consumer:
    def __init__(self, prod):
        self.prod=prod

    def consume(self):
        for i in range(1,6):
            print('Item received', self.prod.q.get(i))

p=Producer()
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()