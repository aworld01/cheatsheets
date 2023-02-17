"""
This method is used to remove last element from existing array.
Syntax:- array_name.pop()
"""

# from array import *
# stu_roll = array('i', [101, 102, 103, 104, 105])
# print(f'Before pop: {stu_roll}')

# stu_roll.pop()
# print(f'After pop: {stu_roll}')



"""
This method is used to remove an element specified by position number, from the existing array and returns removed element.
Syntax: array_name.pop(position_number)
"""

from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
print(f'Before pop: {stu_roll}')

r = stu_roll.pop(2)
print(f'After pop: {stu_roll}')
print('Removed item:', r)