"""
A list represents a group of elements.
Lists are mutable so we can modify it's element.
"""
# # Creating a list
# l = [] #empty list
# print(l)

a = [10,20,-50,21.3, 'ArtificialWorld']
# print(a)




# # Indexing
# """
# a[0]=10
# a[1]=20
# a[2]=-50
# a[3]=21.3
# a[4]='ArtificialWorld'

# a[-1]='ArtificialWorld'
# a[-2]=21.3
# a[-3]=-50
# a[-4]=20
# a[-5]=10
# """
# print(a[3])
# print(a[-3])




# # # update list
# print(a)
# a[1] = 40
# print(a)



# # check address
print(a, id(a))
a[1] = 40
print(a, id(a))