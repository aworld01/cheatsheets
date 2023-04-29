"""
A variable is nothing but a reserved memory location to store values.
In other words a variable in a program gives data to the computer to work on.
05:00 / 17:00
"""

"""example-1"""
# a = "Hello world!"
# b = 5
# c = 2.4

"""to check datatype"""
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
"""to check memory location"""
# print(a, id(a))
# print(b, id(b))
# print(c, id(c))



"""example-2"""
# a = "Hello world!"
# print(a, id(a)) #to check memory location

# a = "Hello world!"
# print(a, id(a))

# a = "Hi there!"
# print(a, id(a))



"""example-3"""
a = 5; b = 6; c = 10 #example1
x, y, z = 4, 6, 11 #example2

print(a)
print(b)
print(c)
print(x)
print(y)
print(z)


del a #the variable will no more can be use (porpose to free memory)