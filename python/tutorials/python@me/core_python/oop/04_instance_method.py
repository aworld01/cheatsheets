class A:
    def __init__(self):
        self.name = "Abdul Zoha"
        self.age = 28
    """creating instance_method"""
    def show(self):
        print(f"Your name is {self.name} you are {self.age} years old")
a = A()
a.show()