"""This method returns a sequence of values from the dictionary."""

students = {101:'Rahul',102:'Raj',103:"Sonam"}
print(students)
print()

"""method-1"""
# values = students.values()
# print(values)
# list_key = list(values) #to convert into list
# print(list_key)

"""method-2"""
for value in students.values():
    print(value)