"""
This method is used to insert an element in a particular position of the existing array.
Syntax:- array_name.insert(position_number, new_element)
"""

# from array import *
# stu_roll = array('i', [101, 102, 103, 104, 105])
# n = len(stu_roll)
# for i in range(n):
#     print(f"{i} = {stu_roll[i]}")



from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)
for i in range(n):
    print(f"{i} = {stu_roll[i]}")
print()

stu_roll.insert(1,777)
for i in range(n):
    print(f"{i} = {stu_roll[i]}")