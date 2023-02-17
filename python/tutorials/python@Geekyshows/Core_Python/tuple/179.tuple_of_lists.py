# a = (10,20,[30,40])
# print(f'Tuple: {a}')
# print(f'Id: {id(a)}')
# print(f'Type: {type(a)}')
# print()

# Modifying list of tuple.
# a = (10,20,[30,40])
# print(f'Original tuple: {a}')
# print(f'Id: {id(a)}')
# print(f'Type: {type(a)}')
# print()
# a[2][0] = 90
# print(f'After modifying the list of tuple: {a}')
# print(f'Id: {id(a)}')
# print(f'Type: {type(a)}')

# # Accessing list of tuple using for loop
# a = [10,20,(30,40)]
# n = len(a)
# for i in range(n):
#     if type(a[i]) is list:
#         if len(a[i])>1:
#             m = len(a[i])
#             for j in range(m):
#                 print(i,j, a[i][j])
#     else:
#         print(i, a[i])




# a = ([10,20,30],[40,50,60])
# print(f'Original tuple: {a}')
# a[0][0] = 80
# print(f'After modification: {a}')

a = [(10,20,30),(40,50,60)]
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j, a[i][j])
    print()