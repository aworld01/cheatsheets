"""
This method returns the value of the specified key.
If key is not found then it will return none or default value.
Syntax: dict.get(key,defaultvalue)
"""

st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Original dictionary',st)
d = st.get(101,'Value is not found....')
print(d)

st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Original dictionary',st)
d = st.get(100,'Value is not found....')
print(d)