"""This method is used to update the dictionary with the specified key value pair."""

# """method-1"""
# students = {101:'Rahul',102:'Raj',103:"Sonam"}
# print(students)

# students.update({104:"Rohan"}) #to update a single item
# print(students)

# students.update({102:"Sarfaraj"}) #replace if already exist
# print(students)




"""method-2"""
students = {101:'Rahul',102:'Raj',103:"Sonam"}
print(students)

"""update multiple items"""
details = {"Name":"Rahul", "Address":"Ranchi"}
students.update(details)
print(students)