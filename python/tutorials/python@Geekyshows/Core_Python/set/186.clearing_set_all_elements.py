# # clear() method is used to remove all elements to the set.

a = {10,20,'ArtificialWorld'}
print('Before clear: ',a)
print(id(a))
b = a.clear()
print('After clear: ',a)
print(id(a))