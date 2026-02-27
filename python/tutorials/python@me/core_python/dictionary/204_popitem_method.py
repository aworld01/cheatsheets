"""
This method is used to remove the item which was last inserted into the dictionary.
It returns the removed item in the form of tuple, Pairs are returned in LIFO (Last In First Out) order.
Syntax:- dict_name.popitem()
Ex:- st.popitem()
"""

students = {101:"Rahul", 102:"Raj", 103:"Sonam"}
print(f"Before removing: {students}")
a = students.popitem()
print(f"After removing: {students}")
print(f"Poped item: {a}")