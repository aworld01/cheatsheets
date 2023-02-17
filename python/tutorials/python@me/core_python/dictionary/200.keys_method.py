"""This method returns a sequence of keys from the dictionary."""

students = {101:'Rahul',102:'Raj',103:"Sonam"}
print(students)
print()

"""method-1"""
# keys = students.keys()
# print(keys)
# list_key = list(keys) #to convert into list
# print(list_key)

"""method-2"""
for key in students.keys():
    print(key)