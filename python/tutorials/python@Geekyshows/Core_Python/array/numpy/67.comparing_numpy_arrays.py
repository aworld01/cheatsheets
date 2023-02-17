"""
Relational operators are used to compare the value of operands (expressions) to produce a logical value. A logical value is either True or False.
Comparison operators can be used to compare arrays. The size of array must be same. Comparison operators compares the corresponding elements of the arrays and returns another array with the Boolean values.
Example:-
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
c = a == b
"""

from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
result = a == b
print(result)

from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
result = a < b
print(result)

from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
result = a > b
print(result)