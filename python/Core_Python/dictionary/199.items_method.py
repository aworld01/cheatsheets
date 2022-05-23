"""
This method returns an object that contains key-value pairs of dictionary.
The pairs are stored as tuple in the object.
"""

# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dict: ',st,type(st))
# it = st.items() #to get list items
# print(it,type(it))

# # Convert into list
# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dict: ',st,type(st))
# it = st.items()
# print(it,type(it))
# lst = list(it) #to convert into list
# print(lst,type(lst))

# # Access list items
st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Original dict: ',st,type(st))
it = st.items()
print(it,type(it))
lst = list(it) #to convert into list
print(lst,type(lst))
a = lst[0] #to access index of zero element
print(a)
b = lst[0][0] #to access index of zero zero element
print(b)
c = lst[0][1] #to access index of zero one element
print(c)
d = lst[1] #to access index of one element
print(d)