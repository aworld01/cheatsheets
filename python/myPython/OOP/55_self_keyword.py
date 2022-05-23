class Employee:
    no_of_leaves = 8

    """creating a method"""
    def details(self):
        return f"name is {self.name}, salary is {self.salary} and role is {self.role}"

harry = Employee()
rohan = Employee()

"""creating instance variables for harry"""
harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

"""creating instance variables for rohan"""
rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

"""calling details method"""
print(harry.details())
print(rohan.details())