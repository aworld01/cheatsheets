"""
Slicing on arrays can be used to retrieve a piece of the array that contains a group of elements. Slicing is useful to retreive a range of elements.
Syntax:- new_array_name = array_name[start:stop:stepsize]
"""

# # Slice from 1st position to 4th position.
from array import *
stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107])
print(f'Original array\n{stu_roll}')
print()
a = stu_roll[1:5]
print(f'Slice from 1st position to 4th position:\n{a}')
print()

# # Slice from 0th position to last position.
b = stu_roll[0:]
print(f'Slice from 0th position to last position:\n{b}')
print()

# # Slice from 3rd position to last position.
c = stu_roll[3:]
print(f'Slice from 3rd position to last position:\n{c}')
print()

# # Slice from 0th position to 4th position.
d = stu_roll[:5]
print(f'Slice from 0th position to 4th position:\n{d}')
print()

# # Slice only 4th element from last.
e = stu_roll[-4]
print(f'Slice only 4th element from last:\n{e}')
print()

# # Slice last 4 elements.
f = stu_roll[-4:]
print(f'Slice last 4 elements:\n{f}')
print()

# # Slice -5-(-3) elements.
g = stu_roll[-5:-3]
print(f'Slice -5-(-3) elements:\n{g}')
print()

# # Slice -6-(-2) elements.
h = stu_roll[-6:-2]
print(f'Slice -6-(-2) elements:\n{h}')
print()

# # Slice elements after skip 2 elements.
i = stu_roll[0:7:2]
print(f'Slice -6-(-2) elements:\n{i}')
print()