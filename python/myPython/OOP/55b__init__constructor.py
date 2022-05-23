class Employee:
    no_of_leaves = 0

    def __init__(self, name, salary, role): #constructor
        self.name = name
        self.salary = salary
        self.role = role

    def details(self):
        return f"The name is {self.name}, salary is {self.salary} and the role is {self.role}"

"""passing arguments"""
harry = Employee("Harry", 455, "Instructor")
rohan = Employee("Rohan", 4554, "Student")

"""calling instance-variables"""
print(harry.name)
print(harry.salary)
print(harry.role)
print()

"""calling instance-method"""
print(harry.details())
print(rohan.details())