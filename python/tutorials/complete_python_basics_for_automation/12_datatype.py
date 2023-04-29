"""
Every value in python has a datatype.
Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.
"""
string = "Hello world" #string
"""boolean"""
boolean1 = True
boolean2 = False
"""number"""
num = 123
flt = 2.5
com = 3+4j

"""to check datatype"""
# print(f"{string} => {type(string)}")
# print(f"{boolean1} => {type(boolean1)}")
# print(f"{boolean2} => {type(boolean2)}")
# print(f"{num} => {type(num)}")
# print(f"{flt} => {type(flt)}")
# print(f"{com} => {type(com)}")


"""printing informations"""
# print(f"Data => {string}") #print variable
# print(f"Type => {type(string)}") #to check datatype
# print(f"Memory location => {id(string)}") #to check memory location



"""
TYPE CASTING
============
Any datatype can be converted into boolean datatype.
Any datatype can be converted into string but reverse is not always True.

nonEmptyData = True (boolean)
emptyData = False (boolean)

EMPTY DATA
==========
0, None, string"", list[], tuple(,), dict{:}, set{}
"""
h = "Hello world!"
x = 5
y = "6"
"""check datatype"""
# print(f"{h} => {type(h)}")
# print(f"{x} => {type(x)}")
# print(f"{y} => {type(y)}")
# print()

"""after type casting"""
# h = bool(h)
# x = str(x)
# y = int(y)
"""check datatype"""
# print(f"{h} => {type(h)}")
# print(f"{x} => {type(x)}")
# print(f"{y} => {type(y)}")



"""Any datatype can be converted into string."""
i = True
print(i, type(i))
j = str(i)
print(j, type(j))