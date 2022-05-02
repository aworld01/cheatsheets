# # Slicing on list can be used retrieve a piece of the list that contains a group of elements. Slicing is useful to retrieve a range of elements.

# x = [101,102,103,104,105,106,107]
# print('Original list:', x)
# print('From 1st position to 4th position:', x[1:5])
# print('From 0th position to last position:', x[0:])
# print('From 0th position to 4th position:', x[:5])
# print('Last 4 elements:', x[-4:])
# print('From 0th position to 6th position stride 2:', x[0:7:2])
# print('Last 5 elements with [-5(-3)] = 2 elements towards right',x[-5:-3])

x = [55,89,5,45,98,12,6,34,86,34]
print('From 0th position to 6th position stride 2:',x[0:7:2])