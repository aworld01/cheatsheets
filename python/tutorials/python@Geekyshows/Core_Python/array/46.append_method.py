"""
This method is used to add an element at the end of the existing array.
Syntax:- array_name.append(new_element)
"""
from array import *
stu_roll = array('i',[101,102,103,104,105])
print('Before appending: ',stu_roll)
stu_roll.append(106)
print('After appending: ',stu_roll)