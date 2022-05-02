class Employee:
    no_of_leaves = 8

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def details(self):
        return f"The name is {self.name}. Salary is {self.salary} the role is {self.role} and Numbers of leave: {self.no_of_leaves}"

    @classmethod # to access class variable
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

harry = Employee("Harry", 255, "Instructor")

print(harry.details()) #to call details method

# Employee.no_of_leaves = 20 #to change class variable

# harry.change_leaves(30) #can change by instance
Employee.change_leaves(23) #can change by class

print(f"Numbers of leave in class {Employee.no_of_leaves}")