# # We can delete element using remove() or discard() methods.
# # Remove() method raise an error if element does't exists while discard() method remains unchanged.

# a = {10,20,30,'ArtificialWorld'}
# print('Original set: ',a)
# print()
# a.remove(20)
# print('After removing set: ',a)

# a = {10,20,30,'ArtificialWorld'}
# a.remove(50) #This will raise a KeyError.
# print('After removing set: ',a)



# a = {10,20,30,'ArtificialWorld'}
# a.discard(50) #This will raise any Error.
# print('After removing set: ',a)