"""
This method returns position number of first occurrence of given element in the array. If it doesn't found the element, shows ValueError.
Syntax:- array_name.index(element)
"""

from array import *
stu_roll = array('i', [101, 102, 101, 104, 105])
l = stu_roll.index(101)
print('Index:', l)