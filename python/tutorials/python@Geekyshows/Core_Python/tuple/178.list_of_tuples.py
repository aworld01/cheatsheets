# a = [10,20,(30,40)]
# print(f'List: {a}')
# print(f'Id: {id(a)}')
# print(f'Type: {type(a)}')
# print()

# # Appending a new tuple of list.
# a = [10,20,(30,40)]
# print(f'Original list: {a}')
# print(f'Id: {id(a)}')
# print(f'Type: {type(a)}')
# print()
# a.append((50,60))
# print(f'After appending the tuple of list: {a}')
# print(f'Id: {id(a)}')
# print(f'Type: {type(a)}')

# # Accessing tuple of list using for loop
# a = [10,20,(30,40)]
# n = len(a)
# for i in range(n):
#     if type(a[i]) is tuple:
#         if len(a[i])>1:
#             m = len(a[i])
#             for j in range(m):
#                 print(i,j, a[i][j])
#     else:
#         print(i, a[i])




# a = [(10,20,30),(40,50,60)]
# print(f'Original List: {a}')
# a.append((70,80))
# print(f'After modification: {a}')
# a.append([90,100])
# print(f'After more modification: {a}')

a = [(10,20,30),(40,50,60)]
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j, a[i][j])
    print()