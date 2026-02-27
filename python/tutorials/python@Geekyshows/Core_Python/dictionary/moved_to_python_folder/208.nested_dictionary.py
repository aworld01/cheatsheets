"""
A dictionary within another dictionary is called as nested dictionary or nesting of a dictionary.
Syntax:- nested_dict = {'Dict1': {'Key_A':'Value_A'},
                        'Dict2': {'Key_B':'Value_B'}
                        }
                                           
Creating empty nested dict
Syntax: - nested_dict = {'Dict1':{},
                         'Dict2':{}
                        }
"""

# # Accessing Dictionary
# a = {'Course':'Python','Fees':15000, 1:{'Course':'JavaScript','Fees':10000}}
# print(a)
# print(a['Course'])
# print(a[1])
# print(a[1]['Fees'])



# # Modifying nested Dictionary
# a = {'Course':'Python','Fees':15000, 1:{'Course':'JavaScript','Fees':10000}}
# print(a)
# a['Course'] = 'Machine Learning'
# print(a)
# a[1]['Fees'] = 25000
# print(a)



# # Deleting nested Dictionary
# a = {'Course':'Python','Fees':15000, 1:{'Course':'JavaScript','Fees':10000}}
# print(a)
# del a[1]['Course']
# print(a)



# # Adding nested Dictionary
# a = {'Course':'Python','Fees':15000, 1:{'Course':'JavaScript','Fees':10000}}
# print(a)
# a[1]['Duration'] = '6 Months'
# print(a)



# # Adding a Dictionary into nested Dictionary
# a = {'Course':'Python','Fees':15000, 1:{'Course':'JavaScript','Fees':10000}}
# print(a)
# a[2] = {'Course':'ReactsJS','Fees':30000}
# print(a)

a = {'Course':'Python','Fees':15000, 1:{'Course':'JavaScript','Fees':10000}}
print(a)
a[1][2] = {'Course':'ReactsJS','Fees':30000}
print(a)