"""
This method returns the value of the specified key.
If key is not found then it inserts key with the specified value.
Syntax:- dict_name.setdefault(key,value)
Ex:- st.setdefault(109,'Rohit')
"""

students = {101:"Rahul", 102:"Raj", 103:"Sonam"}
print(students)

"""example-1"""
# returned_value = students.setdefault(102) #This will return found value
# print(f"Returned value: {returned_value}")

"""example-2"""
returned_value = students.setdefault(104,"Abdul Zoha") #This will return default value because its not found
print(f"Returned value: {returned_value}")