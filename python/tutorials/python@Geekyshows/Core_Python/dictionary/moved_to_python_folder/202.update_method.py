"""
Syntax:- dict_name.update(iterable)
Ex:- stu.update({105:'Gupchup'})
"""

# # To update a single item
# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dict: ',st)
# print(id(st))
# st.update({104:'Python'}) #to update a single item
# print('Updated dict: ',st)
# print(id(st))

# # To update multiple items
st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Original dict: ',st)
print(id(st))
 #to update multiple items
val = {'Name':'Rahul','Address':'Ranchi',105:'ArtificialWorld'}
st.update(val)
print('Updated dict: ',st)
print(id(st))
