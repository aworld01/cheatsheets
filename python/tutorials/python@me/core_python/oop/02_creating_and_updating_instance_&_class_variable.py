class Employee:
    pass
    
harry = Employee() #creating instance
rohan = Employee()

"""creating variables"""
Employee.no_of_leaves = 8 # creating class variable
harry.name = "Harry" #creating instance_variable
rohan.name = "Rohan"
rohan.no_of_leaves = 9 #creating instance_variable with same name of class_variable

print("\tBefore changing...")
"""accessing variables"""
print(f"Class items:\n{Employee.__dict__}") #printing class items
print()
print(f"Instance variables:\n{harry.__dict__}") #printing instance variables
print(rohan.__dict__)
print()

"""updating variables"""
Employee.no_of_leaves = 10 #to change the class_variable
rohan.no_of_leaves = 11 #to change the instance_variable

print("\tAfter changing...")
print(f"Class items:\n{Employee.__dict__}") #printing class_items
print()
print(f"Instance variables:\n{harry.__dict__}") #printing instance variables
print(rohan.__dict__)
