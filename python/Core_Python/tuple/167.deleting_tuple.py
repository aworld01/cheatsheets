# # You can delete entire tuple but not an element of tuple.
# a = (10,20,-50,21.3,'ArtificialWorld')
# print(a)

# del a
# print(a)



# a = (10,20,-50,21.3,'ArtificialWorld')
# tup1 = a[:3]
# print(a, id(a))
# print(tup1, id(tup1))

a = (10,20,-50,21.3,'ArtificialWorld')
print(a)
tup1 = a[:3]
print(tup1)
tup2 = a[4:]
print(tup2)
result = tup1 + tup2
print(result)