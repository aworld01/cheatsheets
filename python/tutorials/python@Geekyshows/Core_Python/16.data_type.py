# # You can see the type of data using 'type()' function:-

# # Numeric type (int, float, complex)
# # Assigning the variables
a = 10
b = 10.5
c = 5 + 7j
d = True
e = None

# # Printing the variables
# print(a)
# print(b)
# print(c)
# print()

# # Printing the type of variables
# print(type(a))
# print(type(b))
# print(type(c))









# # int
# a = 10
# print(a, type(a))

# #float
# b = 10.5
# print(b, type(b))

# #complex
# c = 5 + 7j
# print(c, type(c))




# Sequence type (string, list, tuple, range)

# # string
# name = "Abdul Zoha"
# print(name, type(name))

# #list
# items = ['Apple', 'Banana', 'Orange', 20, 25.5]
# print(items, type(items))

# # tuple
# items = ('Apple', 'Banana', 'Orange', 20, 25.5)
# print(items, type(items))

# # range
# a = range(5)
# print(a[2], type(a))

# # set
# items = {'Apple', 'Banana', 'Orange', 20, 25.5, 20}
# print(items, type(items))

# mapping / dict
# data = {'Apple':'Seb', 'Mango':'Aam'}
# print(data, type(data))

# print(data['Apple'])


##floating point value slicing
a=3.5215926796797877
print(f'Oringinal_data: {a}')
print(type(a))
print()

b=f'{a:.1f}' #to slice from float into string.
print(f'To slice into float to string: {b}')
print(type(b))
print()

c=float(f'{a:.1f}') #to slice from float into float.
print(f'To slice into float to string: {c}')
print(type(c))