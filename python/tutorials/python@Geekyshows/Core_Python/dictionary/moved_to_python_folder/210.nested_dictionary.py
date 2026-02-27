# # Accessing nested dictionary
# a = {1:{'Course':'Python','Fees':15000},
#      2:{'Course':'JavaScript','Fees':10000}}
# print(a)
# print(a[1])
# print(a[2])
# print(a[1]['Course'])
# print(a[2]['Fees'])

# # Modifying nested dictionary
# a = {1:{'Course':'Python','Fees':15000},
#      2:{'Course':'JavaScript','Fees':10000}}
# print(a)
# a[1]['Course'] = 'Machine Learning' #to modify the Course of a[1].
# print(a)
# a[2]['Fees'] = 25000 #to modify the Fees of a[2].
# print(a)

# # Deleting nested dictionary
# a = {1:{'Course':'Python','Fees':15000},
#      2:{'Course':'JavaScript','Fees':10000}}
# print(a)
# del a[1]['Fees'] #to delete the Fees of a[1].
# print(a)

# # Adding a new item in dictionary
# a = {1:{'Course':'Python','Fees':15000},
#      2:{'Course':'JavaScript','Fees':10000}}
# print(a)
# a[2]['Duration'] = '6 months' #to add a new item in dictionary.
# print(a)

# # Adding a new dictionary in dictionary
# a = {1:{'Course':'Python','Fees':15000},
#      2:{'Course':'JavaScript','Fees':10000}}
# print(a)
# a[3] = {'Course':'WebDesigning','Fees':8000} #to add a new dictionary in dictionary.
# print(a)
