"""
A Dictionary represents a group of elements in the form of key value pairs.
Dictionary in python is an unordered collection.
Dictionaries are mutable so we can modify it's item, without changing their identity.
Dictionaries are represented using curly bracket {}.

A Dictionary is created in the form of key-value pair where keys can't be repeated and must be immutable and values can be of any datatype and can be duplicated.
Keys are case sensitive.

We can access the value of a dictionary by referring to its key name, inside square brackets.
ex:- a = {101:'Rahul', 102:'Raj', 103:'Sonam'}
print(a[101])

While writing key we must follow the following rules:
Key should be unique.
If we mention same key again, the old key will be overwritten.
Key should be immutable type ex:- integer, string, or tuple.
We can't use list or dictionary as a key.
"""


# a = {} #Creating an empty Dictionary
# print(a, type(a))

a = {101:'Rahul', 102:'Raj', 103:'Sonam'} #Create a Dictionary
# print(a, type(a))

print(a[102]) #Accessing Dictionary item
print(a[101])