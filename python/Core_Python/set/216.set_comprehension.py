"""
Set comprehension represents creation of a new set from an iterable object that satisfy a given condition.
There can be zero or more If statements.
There can be one or multiple for loops.
Syntax:- new_set = {expresion for item in iterable_object if_statement}
Example:- set1 = {i+1 for i in range(20)}
Example:- set2 = {i for i in range(20) if i%2==0}
Example:- set3 = {i for i in range(11) if i%2==0 if i%3==0}
"""

# set1 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
# new_set1 = set() #to make an empty set.
# for i in set1:
#   new_set1.add(i+1)
# print(new_set1)

# # set comprehension
# set2 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
# new_set2 = {i+1 for i in set2}
# print(new_set2)



# # With range() function
# new_set1 = set() #to make an empty set.
# for i in range(20):
#   new_set1.add(i+1)
# print(new_set1)

# # set comprehension
# new_set2 = {i+1 for i in range(20)}
# print(new_set2)



# set1 = set()
# for i in range(20):
#   if i%2==0:
#     set1.add(i)
# print(set1)

# # set comprehension
# set2 = {i for i in range(20) if i%2==0}
# print(set2)



# set1 = set()
# for i in range(20):
#   if i%2==0:
#     if i%3==0:
#       set1.add(i)
# print(set1)

# # set comprehension
# set2 = {i for i in range(20) if i%2==0 if i%3==0}
# print(set2)




"""
Set comprehension with If else statement...
Syntax:- new_set = {expression if_statement else_expression for item in iterable_object}
Example:- new_set = {i if i%2==0 else i*1000 for i in range(10)}
"""

# set1 = set()
# for i in range(10):
#   if i%2==0:
#     set1.add(i)
#   else:
#     set1.add(i*1000)
# print(set1)

# # set comprehension
# set2 = {i if i%2==0 else i*1000 for i in range(10)}
# print(set2)