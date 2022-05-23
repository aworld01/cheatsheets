class A:
    def details1(self):
        print(f"My name is Abdul Zoha,\nI'm 28 years old now.\nI'm from Chandpali.")

# me = A()
# me.details1()

class B(A):
    def __init__(self, name, age, vill, dist):
        self.name = name
        self.age = age
        self.vill = vill
        self.dist =dist
    def details2(self):
        print(f"My name is {self.name},\nI'm {self.age} years old now.\nMy village is {self.vill}.\nMy Distric is {self.dist}.")

me2 = B("Abdul Zoha", 29, "Chandpali", "Siwan") #making object of class B
me2.details1() #calling class A's details1 method
print()
me2.details2() #calling class B's details2 method