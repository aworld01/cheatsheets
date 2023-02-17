"""
This method returns the value of the specified key.
If key is not found then it will return none or default value.
"""

"""example-1"""
# students = {101:"Rahul", 102:"Raj", 103:"Sonam"}
# print(f"Original dictionary: {students}")

# new_students = students.get(100)
# print(new_students)

"""example-2"""
# students = {101:"Rahul", 102:"Raj", 103:"Sonam"}
# print(f"Original dictionary: {students}")

# new_students = students.get(101, "Value is not found...")
# print(new_students)


"""example-3"""
students = {101:"Rahul", 102:"Raj", 103:"Sonam"}
print(f"Original dictionary: {students}")

new_students = students.get(100, "Value is not found...")
print(new_students)