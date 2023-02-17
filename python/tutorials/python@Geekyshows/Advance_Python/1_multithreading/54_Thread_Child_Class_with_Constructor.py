from threading import *
##Example-1
# class MyThread(Thread): #Thread Class as Parent Class
#     def __init__(self):
#         Thread.__init__(self) #Calling Thread Class Constructor
#         print('Child Thread Constructor')

#         def run(self):
#             pass
# t=MyThread()
# t.start()
# print('Main Thread')


##Example-2
class MyThread(Thread): #Thread Class as Parent Class
    def __init__(self, a):
        Thread.__init__(self) #Calling Thread Class Constructor
        print('Child Thread Constructor:', a)

        def run(self):
            pass
t=MyThread(20)
t.start()
print('Main Thread')