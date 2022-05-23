"""
We can delete an item of dictionary or entire dictionary using del statement.
"""

# # to delete an item of dictionary
# st = {101:'Rahul',102:'Raj',103:'Sonam'}
# print('Before deletion: ', st)
# print(id(st))
# print()
# del st[102] #deleting an item.
# print('After deletion: ',st)
# print(id(st))

# # to delete entire dictionary
st = {101:'Rahul',102:'Raj',103:'Sonam'}
print('Before deletion: ', st)
del st #to delete entire dictionary
print(st)