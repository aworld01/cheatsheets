'''
In multi-level inheritance, the class inherits the feature of another derived class (Child-class).
'''

# class Father:
#     def show(self):
#         print("Father class instance-method")
# class Son(Father):
#     def showS(self):
#         print("Son class instance-method")
# class GrandSon(Son):
#     def showG(self):
#         print("Grand-son class instance-method")

# s = GrandSon()
# s.show()
# s.showS()
# s.showG()



##Multi-inheritance with constructor
class Father:
    def __init__(self):
        print("Father class constructor have called")

    def show(self):
        print("Father class instance-method")
class Son(Father):
    def __init__(self):
        super().__init__() #calling Parent class constructor
        print("Son class constructor have called")

    def showS(self):
        print("Son class instance-method")
class GrandSon(Son):
    def __init__(self):
        super().__init__() #calling Son class constructor
        print("GrandSon class constructor have called")

    def showG(self):
        print("Grand-son class instance-method")

s = GrandSon()
s.show()
s.showS()
s.showG()