a = {'Course':'Python','Fees':15000, 1:{'Course':'JavaScript','Fees':10000}}
#print(a)

# # Accessing each id keys -- value
for i in a:
  if type(a[i]) is dict:
    for k in a[i]:
      print(f'{k} = {a[i][k]}')
  else:
    print(f'{i} = {a[i]}')