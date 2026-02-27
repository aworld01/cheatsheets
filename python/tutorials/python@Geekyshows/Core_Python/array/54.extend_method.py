"""
This method is used to append another array or iterable object at the end of the array.
Syntax:- array_name.extend(arr)
"""

from array import *
stu_roll = array('i', [101, 102, 103, 104, 105])
arr = array('i', [107, 108, 109])
print('Original array: ', stu_roll)
print()
stu_roll.extend(arr)
print('After reverse: ', stu_roll)