"""
set datatype
set is unordered collection of unique items

You can store in set:-
string, integer, float

You can't store in set:-
list, dictionary, tuple
"""
# s = {1,2,3,2}
# print(s, type(s))



"""we can use set to remove duplicate items"""
# l = [1,2,3,4,5,5,5,6,7,7,8]
# print(l)
# s = list(set(l)) #to remove duplicate items
# print(s)


"""add items in set"""
# s = {1,2,3}
# print(s)

# s.add(5) #to add item
# s.add(8)
# print(s)


"""remove items in set"""
s = {1,2,3,5,8}
print(s)

# s.remove(2) #to remove item
# print(s)

# s.discard(9) #to get rid of KeyError
# print(s)

# s.clear() #to clear the set
# print(s)

s2 = s.copy() #to copy the set
print(s, id(s))
print(s2, id(s2))