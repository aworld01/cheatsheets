"""
any () function: This function returns True, if any one element of the iterable is True. If iterable is empty then returns False.
Example:-
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
c = a == b
any(c)
"""

from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
result = a == b
print(any(result))



"""
all () function: This function returns True, if all element of the iterable are True or iterable is empty.
Example:-
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
c = a == b
all(c)
"""

from numpy import *
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])
result = a == b
print(all(result))