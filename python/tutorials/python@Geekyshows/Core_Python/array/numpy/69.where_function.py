"""
where () function: This function is used to create a new Array which contains, returned element chosen from expression1 or expression2 depending on condition. If condition is True expression1 is executed else expression2.
Example:-
a = array([100, 200, 300, 400, 500])
b = array([10, 201, 30, 40, 50])
c = where(a>b, a,b)
"""

from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
result = where(a>b, a,b)
print(result)

from numpy import *
a = array([101, 12, 300, 4, 500])
b = array([100, 20, 30, 400, 50])
result = where(a>b, a,b)
print(result)