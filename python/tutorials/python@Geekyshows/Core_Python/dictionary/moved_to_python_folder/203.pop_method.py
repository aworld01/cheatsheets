"""
This method is used to remove the item with specified key.
It returns the removed item's value.
If key is not found then a value is returned.
If key is not found and default value is not given then shown KeyError.
Syntax:- dict_name.pop(key,defaultvalue)
Ex:- st.pop(101)
Ex:- st.pop(101,'Key is not found')
"""

# st = {101:'Rahul',102:'Raj',103:"Sonam"}
# print('Before pop: ',st)
# a = st.pop(102)
# print('After pop: ',st)
# print('Poped item: ',a)

st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Before pop: ',st)
a = st.pop(104,'The key is not found....')
print('After pop: ',st)
print('Poped item: ',a)
