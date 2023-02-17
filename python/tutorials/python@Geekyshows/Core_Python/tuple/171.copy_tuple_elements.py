# # We can copy elements of tuple into another tuple using slice.
a = (10,20,30,40,50)
b = a #To aliasing tuple
print(a, id(a))
print(b, id(b))
c = a[:5] #If you slice full object then data will be not copy.
print(c, id(c))
d = a[:4] #If you slice less object then data will be copy.
print(d, id(d))