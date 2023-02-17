"""
nonzero () function: This function is used to determine the position of elements which are non zero. This function returns an array that contains the indexes of the element of the array which are not equal to zero.
Example:-
a = array([100, 200, 13, 0, 400, 500, 0])
result = nonzero(a)
"""

from numpy import *
a = array([100, 200, 13, 0, 400, 500, 0])
result = nonzero(a)
print(result)