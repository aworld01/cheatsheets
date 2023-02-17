"""
This method is used to remove first occurrence of given element from the existing array. If it doesn't found the element, shows ValueError.
Syntax:- array_name.remove(element)
"""

from array import *
stu_roll = array('i', [101, 102, 103, 104, 105, 101])
print(f'Before remove: {stu_roll}')

stu_roll.remove(101)
print(f'After remove: {stu_roll}')