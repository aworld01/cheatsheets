#a = {1:{'Course':'Python','Fees':15000},
#     2:{'Course':'JavaScript','Fees':10000}}
#print(a)
#print()

#for id in a:
#  print('ID: ',id)
#print()

#for id in a:
#  for key in a[id]:
#    print('Key: ',key)


a = {1:{'Course':'Python','Fees':15000},
     2:{'Course':'JavaScript','Fees':10000}}
for id in a:
  for k in a[id]:
    print(k,'=',a[id][k])
print()