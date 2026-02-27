# # copy() method is used to copy all the elements of a list to another list. 
# # When we copy a list a separate copy of all the  elements is stored in another list. Both the list are independent.
# # Modification in a will not affect b and vice versa.

# # copy
#a = [10,20,30,40,50]
#b = a.copy()
#print('Before modification')
#print('This is list A',a)
#print('This is list B',b)
#a[2] = 55

#print()
#print('After modification')
#print('This is list A',a)
#print('This is list B',b)

# # clone
a = [10,20,30,40,50]
b = a[:]
print('Before modification')
print('This is list A',a)
print('This is list B',b)
a[2] = 55

print()
print('After modification')
print('This is list A',a)
print('This is list B',b)