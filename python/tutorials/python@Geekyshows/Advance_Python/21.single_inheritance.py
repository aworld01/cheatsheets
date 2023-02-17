'''
There are four types of Inheritance
1.Single Inheritance
2.Multi-level Inheritance
3.Hierarchical Inheritance
4.Multiple Inheritance

If a class is derived from one Base_class (Parent_class), it's called Single Inheritance.

NOTE:
We can access Parent_class variables and methods using Child_Class_Object.
We can also access Parent_Class_Variables and Methods using Parent_Class_Object
We can not access Child_Class_Variables and Methods using Parent_Class_Object
'''

class Father:
    money = 1000

    def show(self): #Father class instance method
        print('Parent class Instance_method')

    @classmethod
    def showmoney(cls):
        print('Parent class class_method', cls.money)

    @staticmethod
    def stat():
        a = 10
        print('Parent class static_method:', a)

class Son(Father): #Child class instance method
    def disp(self):
        print('Child class instance method')

s = Son() #creating an object of Son_class

s.disp() #accessing Son_class instance method
s.show() #accessing Father_class instance method
s.showmoney() #accessing Father_class class_method
s.stat() #accessing Father_class static_method