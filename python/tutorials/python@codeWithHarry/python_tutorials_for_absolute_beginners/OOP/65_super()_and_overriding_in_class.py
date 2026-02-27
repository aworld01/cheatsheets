"""
ATTRIBUTE OVERRIDING
Instance variable execute first.
"""
# class A:
#     var1 = "I am a class variable in class A" #(3)
#     def __init__(self):
#         pass
#         self.var1 = "I am instance var in class A" #execute first. (1)
# class B(A):
#     pass
#     var1 = "I am a class variable in class B" #execute if instance variable not exist in class A and B. (2)
    
# a = A()
# b = B()

# print(b.var1)





"""example-1"""
# class A:
#     def __init__(self):
#         self.var1 = "I am instance variable in class A"
#         self.var2 = "I am special variable in class A"
# class B(A):
#     def __init__(self):
#         self.var3 = "I am instance variable in class B"
#         self.var4 = "I am special variable in class B"
    
# a = A()
# b = B()
# print(a.var1)
# print(a.var2)
# print(b.var3)
# print(b.var4)



"""super().__init__() #to access super class constructor constructor"""
"""example-2"""
class A:
    def __init__(self):
        self.var1 = "I am instance variable in class A"
        self.var2 = "I am special variable in class A"
class B(A):
    def __init__(self):
        super().__init__() #to access super class constructor constructor
        self.var3 = "I am instance variable in class B"
        self.var4 = "I am special variable in class B"
    
b = B()
print(b.var1)
print(b.var2)
print(b.var3)
print(b.var4)