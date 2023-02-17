# # Aliasing means giving another name to the existing object. It doesn't mean copying.

a = [10,20,30,40,50]
b = a
print(a, id(a))
print(b, id(b))

# mdification in a will affect b and vice versa.
a[3] = 100
print(a)
print(b)