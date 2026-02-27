"""
id() function
type() function
getsizeof() function
"""

a = 10 #(int)
b = 30.23 #(float)
c = "Hello world!" #(str)
d = [10,20,30] #(list)
e = (10,20,30) #(tuple)
f = {10,20,30} #(set)
g = {101:'Rahul',102:'Raj',103:'Sonam'} #(dict)


# #id() function
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# print(id(e))
# print(id(f))
# print(id(g))

# # type function
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))

# getsizeof() function (the size will be in bit)
from sys import getsizeof
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))
print(getsizeof(d))
print(getsizeof(e))
print(getsizeof(f))
print(getsizeof(g))