"""assigning a nested dictionary"""
a = {
    1:{'Course':'Python','Fees':15000},
    2:{'Course':'JavaScript','Fees':10000}
    }
print(a)
print()


"""accessing nested dictionary items"""
# print(a[1])
# print(a[2])
# print(a[1]['Course'])
# print(a[2]['Fees'])


"""modifying nested dictionary items"""
# a[1]['Course'] = 'Machine Learning' #to modify the Course of a[1].
# a[2]['Fees'] = 25000 #to modify the Fees of a[2].
# print(a)


"""deleting nested dictionary items"""
# del a[1]['Fees'] #to delete the Fees of a[1].
# print(a)


"""adding a new item in nested dictionary"""
# a[2]['Duration'] = '6 months' #to add a new item in dictionary.
# print(a)


"""adding a new item in nested dictionary"""
a[3] = {'Course':'WebDesigning','Fees':8000} #to add a new dictionary in dictionary.
print(a)