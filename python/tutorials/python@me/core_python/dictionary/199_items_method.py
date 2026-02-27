"""
This method returns an object that contains key-value pairs of dictionary.
The pairs are stored as tuple in the object.
"""

"""example-1"""
students = {101:'Rahul',102:'Raj',103:"Sonam"}
print(students) #Original dict

# new_students = students.items()
# print(type(new_students)) #to print type of new_students
# print(new_students)


"""example-2"""
students = {101:'Rahul',102:'Raj',103:"Sonam"}
for key, value in students.items(): 
    print(f"Roll is {key} and Name is {value}")