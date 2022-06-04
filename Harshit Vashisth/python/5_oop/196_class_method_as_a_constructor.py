class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def full_name(self):
        print(f"{self.fname} {self.lname}")

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(",")
        return cls(first, last, age)

# p1 = Person("Abdul", "Zoha", 25)
# p1.full_name()

p3 = Person.from_string("Abdul, Zoha, 26")
p3.full_name()