class Person:
    def __init__(self, first_name, last_name, age):
        """instance variabe"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """instance method"""
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def above(self):
        if self.age>18:
            return True


"""instance/object"""
p1 = Person("Harshit", "Vashisth", 16)
p2 = Person("Abdul", "Zoha", 31)

print(p1.full_name())
print(p2.full_name())
print(p1.above())