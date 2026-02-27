class A:
    """instance method"""
    def class_a_method(self):
        print(f"I'm just a class A method")
    def hello(self):
        print(f"Hello from class A")

class B:
    def class_b_method(self):
        print(f"I'm just a class B method")
    def hello(self):
        print(f"Hello from class B")

class C(A, B):
    pass

c = C()
# c.class_a_method()
# c.class_b_method()
# c.hello()

print(help(C)) #to check MethodResolutionOrder

# 03:00 / 09:39