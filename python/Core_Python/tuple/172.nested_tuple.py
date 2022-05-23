# # A tuple within another tuple is called as nested tuple or nesting of a tuple.
# a = (10,20,30,(50,60))
# print(a)

# b = (50,60)
# a = (10,20,30,b)
# print(a)

# a = ((10,20,30),(40,50,60))
# print(a)


# a = (
#     (10,20,30),
#     (40,50,60)
# )
# print(a)


# # Accessing nested tuple
# a = (10,20,30,(40,50))
# print(f'a: {a}')
# print(f'a[0]: {a[0]}')
# print(f'a[1]: {a[1]}')
# print(f'a[2]: {a[2]}')
# print(f'a[3]: {a[3]}')
# print(f'a[3][0]: {a[3][0]}')
# print(f'a[3][1]: {a[3][1]}')

a = ((10,20,30),(40,50,60))
print(f'a: {a}')
print(f'a[0]: {a[0]}')
print(f'a[1]: {a[1]}')
print(f'a[0][0]: {a[0][0]}')
print(f'a[0][1]: {a[0][1]}')
print(f'a[0][2]: {a[0][2]}')
print(f'a[1][0]: {a[1][0]}')
print(f'a[1][1]: {a[1][1]}')
print(f'a[1][2]: {a[1][2]}')