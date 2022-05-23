"""
This method returns a sequence of values from the dictionary.
Syntax: dict_name.values()
"""

# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dict: ',st,type(st))
# all_value = st.values()
# print(all_value, type(all_value))

# # Convert all_value into list
# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dict: ',st,type(st))
# all_value = st.values()
# print(all_value, type(all_value))
# list_value = list(all_value) #to convert dict_values into list
# print(list_value, type(list_value))

# # Access list values
st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Original dict: ',st,type(st))
all_value = st.values()
print(all_value, type(all_value))
list_value = list(all_value) #to convert dict_values into list
print(list_value, type(list_value))
a = list_value[1] #to access list value
print(a)
