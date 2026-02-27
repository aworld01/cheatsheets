# a = (10,20,30,(40,50))
# n = len(a)
# for i in range(n):
#     if type(a[i]) is tuple:
#         if len(a[i])>1:
#             m = len(a[i])
#             for j in range(m):
#                 print(i,j, a[i][j])
#     else:
#         print(i, a[i])




# #Without index
# a = ((10,20,30),(40,50,60))
# for r in a:
#     for c in r:
#         print(c)
#     print()

#With index
a = ((10,20,30),(40,50,60))
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i,j, a[i][j])
    print()