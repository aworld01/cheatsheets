"""
This method returns a sequence of keys from the dictionary.
Syntax: dict_name.keys()
"""

# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dict: ',st)
# d = st.keys() #to get dict keys
# print('keys: ',d)

# # convert into the list
st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Original dict: ',st,type(st))
d = st.keys() #to get dict keys
print('keys: ',d,type(d))
keys_list = list(d) #to convert keys into list.
print(keys_list,type(keys_list))