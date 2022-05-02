"""method: function inside the class is called method.]"""
# """example-1"""
# class Person:
#     def __init__(self):
#         print(f"init method / constructor get called")

# """object"""
# p1 = Person()
# p2 = Person()
# p3 = Person()



"""example-2"""
class Person:
    def __init__(self, first_name, last_name, age):
        """instance variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

"""object"""
p1 = Person("Harshit", "Vashistha", 24)
p2 = Person("Mohit", "Vashistha", 19)

print(p1.first_name)
print(p2.first_name)