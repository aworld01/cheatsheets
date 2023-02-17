# # This method is used to append another list or iterable object at the end of the list.

a = [10,20,30,40,50]
print(f'Before extend: {a}')
b = [60,70,80,90,100]
a.extend(b)
print(f'After extend: {a}')