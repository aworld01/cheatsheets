"""
This method is used to remove the item which was last inserted into the dictionary.
It returns the removed item in the form of tuple, Pairs are returned in LIFO (Last In First Out) order.
Syntax:- dict_name.popitem()
Ex:- st.popitem()
"""

st = {101:'Rahul',102:'Raj',103:"Sonam"}
print('Before removing: ',st)
a = st.popitem()
print('After removing: ',st)
print('Poped item: ',a)
