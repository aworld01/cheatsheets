'''
super(): method is used to call parent class constructor or methods from the child class.
'''

# class Father:
#     def __init__(self):
#         self.money = 2000
#         print("Father class constructor")
#     def show(self):
#         print("Father class instance_method")
# class Son(Father):
#     def __init__(self):
#         super().__init__() #to call Parent_class constructor also.
#         print("Son class constructor")
#     def disp(self):
#         print("Son class instance_method", self.money)

# s = Son()
# s.disp()



## super() method with parameter
class Father:
    def __init__(self, m):
        self.money = m
        print("Father class constructor")
    def show(self):
        print("Father class instance_method")
class Son(Father):
    def __init__(self, m, j):
        super().__init__(m) #to call Parent_class constructor also.
        self.job = j
        print("Son class constructor")
    def disp(self):
        print("Son class instance_method")
        print('Job:', self.job)
        print('Salary:', self.money)

s = Son(10000, 'Python3')
s.disp()