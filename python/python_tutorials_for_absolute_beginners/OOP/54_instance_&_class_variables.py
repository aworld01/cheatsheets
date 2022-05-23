class Employee:
    no_of_leaves = 8 #class_variable
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry" #instance_variable
rohan.name = "Rohan"

"""Accessing class variables"""
print("Harry leaves:",harry.no_of_leaves)
print("Rohan leaves:",rohan.no_of_leaves)
print("Class leaves:",Employee.no_of_leaves)
print()

"""to check variables"""
print("Harry items:",harry.__dict__)
print("Rohan items:",rohan.__dict__)
print("Class items:",Employee.__dict__)
print()

harry.no_of_leaves = 9 #This will make a new instance_variable for harry
print("After changing> harry.no_of_leaves = 9")

"""Accessing class variables"""
print("Harry leaves:",harry.no_of_leaves)
print("Rohan leaves:",rohan.no_of_leaves)
print("Class leaves:",Employee.no_of_leaves)
print()

"""to check variables"""
print("Harry items:",harry.__dict__)
print("Rohan items:",rohan.__dict__)
print("Class items:",Employee.__dict__)
print()

"""Changing class variables"""
Employee.no_of_leaves = 9 #Changing class variable
print("After changing> Employee.no_of_leaves = 9")

"""to check variables"""
print("Harry items:",harry.__dict__)
print("Rohan items:",rohan.__dict__)
print("Class items:",Employee.__dict__)

"""Accessing class variables"""
print("Harry leaves:",harry.no_of_leaves)
print("Rohan leaves:",rohan.no_of_leaves)
print("Class leaves:",Employee.no_of_leaves)
print()