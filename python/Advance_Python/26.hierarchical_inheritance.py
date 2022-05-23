'''
In multi-level inheritance, the class inherits the feature of another derived class (Child-class).
11:30/18:13
'''

class Father:
    def show(self):
        print("Father class instance-method")
class Son(Father):
    def showS(self):
        print("Son class instance-method")
class Daughter(Father):
    def showD(self):
        print("Daughter class instance-method")

s = Son()
d = Daughter()
s.show()
s.showS()
print()
d.show()
d.showD()