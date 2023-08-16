"""simple code"""
# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

"""comprehension"""
# squares2 = [i**2 for i in range(1,11)]
# print(squares2)



"""comprehension with if statement"""
"""simple code"""
# even_nums = []
# for i in range(10):
#     if i%2==0:
#         even_nums.append(i)
# print(even_nums)

"""comprehension"""
# even_nums2 = [i for i in range(10) if i%2==0]
# print(even_nums2)


"""comprehension with if-else statement"""
"""simple code"""
# new_list = []
# for i in range(10):
#     if i%2==0:
#         new_list.append(i*2)
#     else:
#         new_list.append(-i)
# print(new_list)

"""comprehension"""
# new_list2 = [i*2 if i%2==0 else -i for i in range(10)]
# print(new_list2)


"""nested list comprehension"""
"""simple code"""
nested = []
for i in range(1,4):
    nested.append([1,2,3])
print(nested)

"""comprehension"""
nested2 = [[1,2,3] for i in range(1,4)]
print(nested2)