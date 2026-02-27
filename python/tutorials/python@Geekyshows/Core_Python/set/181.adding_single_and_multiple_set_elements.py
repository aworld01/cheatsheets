# # We can add new element to set using add() method.
# # We can add multiple elements to set using update() method. The update() method can take tuples, lists, strings, or other sets as its argument.

# a = {10,20}
# print(a)
# a.add('Abdul Zoha') #to add an element to set.
# print(a)

# a = {10,20}
# print('Before adding: ',a)
# a.update([30,40,50]) #to add multiple elements to set.
# print('After adding: ',a)



a = {10,20}
print('Before adding: ',a)
b = [30,40,50,'ArtificialWorld']
a.update(b) #to add multiple elements to set.
print('After adding: ',a)