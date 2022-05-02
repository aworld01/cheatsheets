# a = {'Rahul','Raj','Sonam','Rani'}
# b = {'Sumit','Rahul','Rani','Python','Java'}
# ism = a.intersection(b) #it will show match values.
# print(ism)

# a = {'Rahul','Raj','Sonam','Rani'}
# b = {'Sumit','Rahul','Rani','Python','Java'}
# i = a.union(b) #return all items from original set and specified set.
# print(i)



# a = {'Rahul','Raj','Sonam','Rani'}
# b = {'Sumit','Rahul','Rani','Python','Java'}
# i = a.difference(b) #returns item that exist only first set not in both set.
# print(i)

# a = {'Rahul','Raj','Sonam','Rani'}
# b = {'Sumit','Rahul','Rani','Python','Java'}
# i = b.difference(a) #returns item that exist only first set not in both set.
# print(i)

# a = {'Rahul','Sonam','Rubi'}
# b = {'Rahul','Raj','Sonam','Rani'}
# i = a.issubset(b) #if all items in the set exist in the specified set.
# print(i)
# a = {'Rahul','Sonam'}
# b = {'Rahul','Raj','Sonam','Rani'}
# i = a.issubset(b) #if all items in the set exist in the specified set.
# print(i)

a = {'Rahul','Raj','Sonam','Rani'}
b = {'Rahul','Sonam','Rubi'}
i = a.issuperset(b) #if all items in the specified set exist in the original set.
print(i)
a = {'Rahul','Raj','Sonam','Rani'}
b = {'Rahul','Sonam'}
i = a.issuperset(b) #if all items in the specified set exist in the original set.
print(i)