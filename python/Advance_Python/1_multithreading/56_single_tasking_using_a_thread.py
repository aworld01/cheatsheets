'''
When multiple tasks are executed by a thread one by one, then it called single tasking.
'''

##method-1
# from threading import Thread
# class MyExam:
#     def solve_question(self):
#         self.q1()
#         self.q2()
#         self.q3()

#     def q1(self):
#         print('Question 1 solved')
#     def q2(self):
#         print('Question 2 solved')
#     def q3(self):
#         print('Question 3 solved')
# mye = MyExam()
# t = Thread(target=mye.solve_question)
# t.start()


##method-2
from threading import Thread
from time import sleep
class MyExam:
    def solve_question(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print('Question 1 solved')
        sleep(3)
    def q2(self):
        print('Question 2 solved')
        sleep(3)
    def q3(self):
        print('Question 3 solved')
mye = MyExam()
t = Thread(target=mye.solve_question)
t.start()