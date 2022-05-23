# # We can modify the existing value of key by assigning a new value.

st = {101:'Rahul',102:'Raj',103:'Sonam'}
print('Before modification: ', st)
print(id(st))
print()
st[102] = 'Kamal' #modify Raj into Kamal.
print('After modification: ',st)
print(id(st))