# # copy() method is used to copy existing set's elements into another set.

a = {10,20,'ArtificialWorld'}
print('Before copy: ',a)
print(id(a))

b = a.copy()
print('After copy: ',b)
print(id(b))