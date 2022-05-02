# # A tuple containsba group of elements which can be same or different types.
# # Tuples are immutable.
# # It's similar to list but Tuples are read-only which means we can't modify it's element.
# # Tuples are used to store data which should not be modified
# # It occupies less memory compare to list
# # Tuples are represented using parentheses ()

##Creating tuple
#a = () #empty tuple.
#print('Empty tuple:',a, type(a))

#b = (10,) #tuple with one element.
#print('Single line tuple:', b, type(b))

#c = (10,20,30,40) #tuple with multiple elements.
#print('Multiple line tuple:',c)

#d = 10,20,30,40
#print(d)


##Indexing tuple
a = (10,20,30,40)
"""
0 = 10
1 = 20
2 = 30
3 = 40
"""
a1 = a[1]
print(a1)

a2 = a[-2]
print(a2)