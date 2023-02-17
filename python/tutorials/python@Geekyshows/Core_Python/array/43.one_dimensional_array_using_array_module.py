"""
One Dimensional Array = Single Row Multiple Comumns
Ex:- [101,102,103,104,105]

There are two ways to import array module:-
import array: This will import the entire array module.
from array import *: This will import all classes, objects, variables etc from array module. Here * means all.


Creating and initializing One-D Array
Method 1.
Syntax:- 
import array
array_name = array.array('type_code',[elements])
Example:- 
import array
stu_roll = array.array('i',[101,102,103,104,105])


Creating and initializing One-D Array
Method 2.
Syntax:- 
from array import *
array_name = array('type_code',[elements])
Example:- 
from array import *
stu_roll = array('i',[101,102,103,104,105])


Creating Empty One-D Array
Syntax:-
from array import *
array_name = array('type_code',[])
Example:-
from array import *
stu_roll = array('i',[])


Index
An index represents the position number of an array's element.
Syntax:-
from array import *
stu_roll = ('i',[101,102,103,104,105])

Index always starts with 0.
stu_roll = ('i',[101,102,103,104,105])
0 = 101
1 = 102
2 = 103
3 = 104
4 = 105

Accessing One-D Array Elements
stu_roll[0] = 101
stu_roll[1] = 102
stu_roll[2] = 103
stu_roll[3] = 104
stu_roll[4] = 105
"""

# import array
# stu_roll = array.array('i',[101,102,103,104,105])
# a = stu_roll[1]
# print(a)

# import array as ar
# stu_roll = ar.array('i',[101,102,103,104,105])
# a = stu_roll[2]
# print(a)

# from array import *
# stu_roll = array('i',[101,102,103,104,105])
# a = stu_roll[3]
# print(a)


from array import *
stu_roll = array('f',[10, 20, 10.3, 40, 1.5]) # you can convert integer into float, but can't float into integer.
print(stu_roll)
