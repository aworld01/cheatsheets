"""
There are two ways to import numpy:-
import numpy: This will import the entire numpy module. (need to write module  name)
ex:-
import numpy
stu_roll = numpy.array([101, 102, 103, 104, 105])

from numpy import *: This will import all class, objects, variable etc from numpy package. Here * means all. (no need to write module name)
ex:-
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])

One Dimensional Array: Single Row Multiple Columns
Ex:- [101, 102, 103, 104, 105]

Ways of creating Array in numpy:-
array() function
linspace() function
logspace() function
arange() function
zeros() function
ones() function

array() function of numpy module is used to create an array.
Syntax:- numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)

Creating 1D Array using array() function:-
Syntax:-
import numpy
array_name = numpy.array([elements])
Ex:-
import numpy
stu_roll = numpy.array([101, 102, 103, 104, 105]) #int datatype
stu_roll = numpy.array([10.1, 10.2, 10.3, 10.4, 10.5]) #float datatype
stu_roll = numpy.array(['a', 'b', 'c', 'd', 'e']) #str datatype
Ex:-
import numpy
stu_roll = numpy.array([101, 102, 103, 104, 105], int) #int datatype
stu_roll = numpy.array([10.1, 10.2, 10.3, 10.4, 10.5], float) #float datatype
stu_roll = numpy.array(['a', 'b', 'c', 'd', 'e'], dtype=str) #str datatype

Index:-
An index represents the position number of an array's element.
Index always starts with 0
Ex:-
stu_roll = array([101, 102, 103, 104, 105])
0 = 101
1 = 102
2 = 103
3 = 104
4 = 105

Accessing One-D Array elements
Ex:-
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

Modifying One-D Array elements
Ex:-
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
print(stu_roll)
stu_roll[2] = 110
print(stu_roll)
"""

# import numpy
# stu_roll = numpy.array([101, 102, 103, 104, 105])
# print(stu_roll)

# from numpy import *
# stu_roll = array([101, 102, 103, 104, 105])
# print(stu_roll)

# from numpy import *
# stu_roll = array([101, 102, 103, 104, 105])
# print(stu_roll.dtype) #to know the type of array

# from numpy import *
# stu_roll = array(['a', 'b', 'c', 'd', 'e'])
# print(stu_roll)


# # Accessing One-D Array elements
# from numpy import *
# stu_roll = array([101, 102, 103, 104, 105])
# print(stu_roll[0])
# print(stu_roll[3])

# # Type casting/conversion
# from numpy import *
# stu_roll = array([101, 102, 103, 104, 105], dtype=float)
# print(stu_roll, stu_roll.dtype)

# # Modifying One-D Array elements
from numpy import *
stu_roll = array([101, 102, 103, 104, 105], dtype=float)
print(stu_roll)
stu_roll[2] = 111
print(stu_roll)

