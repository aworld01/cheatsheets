"""
This method is used to copy all the elements from the existing dictionary into a new dictionary.
"""

students = {101:'Rahul',102:'Raj',103:"Sonam"}
print(f"Original dictionary: {students}")
print(f"{id(students)}")

new_students = students.copy() #to copy dictionary

print(f"Copied dictionary: {new_students}")
print(f"{id(new_students)}")
print()

students[102] = "Ranjan" #to update dictionary

print(f"Original dictionary: {students}")
print(f"Copied dictionary: {new_students}")