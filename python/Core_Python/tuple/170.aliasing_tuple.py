# # Aliasing means giving another name to the existing object. It doesn't mean copying.
a = (10,20,30,40,50)
print(a)
b = a #to aliasing b as a.
print(a, id(a))
print(b, id(b))
a = a[:3]
print(a, id(a))