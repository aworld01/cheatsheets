"""
This method returns the value of the specified key.
If key is not found then it inserts key with the specified value.
Syntax:- dict_name.setdefault(key,value)
Ex:- st.setdefault(109,'Rohit')
"""

# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dict: ',st)
# returned_value = st.setdefault(102) #This will return found value
# print('Returned value: ',returned_value)

# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Original dict: ',st)
# returned_value = st.setdefault(102,'Python') #This will return found value
# print('Returned value: ',returned_value)

st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Original dict: ',st)
returned_value = st.setdefault(109,'Python') #This will return default value because its not found
print('Returned value: ',returned_value)
