# # Tuples are immutable so it's not possible to modify, update or delete it's element.

# a = (10,20,-50,21.3,'ArtificialWorld')
# print(a)
# b = (30,40)
# tup = a+b
# print(tup)

a = (10,20,-50,21.3,'ArtificialWorld')
print(a)
tup = a[:2]
print(tup)
tup2 = a[2:]
print(tup2)
tup3 = (50,60)
print(tup3)
result = tup+tup3+tup2
print(result)