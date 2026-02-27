nums = list(range(10))
print(nums)


"""normal"""
# even_nums = []
# for i in nums:
#     if i%2 == 0:
#         even_nums.append(i)
# print(even_nums)


"""list comprehension"""
even_nums = [i for i in nums if i%2 == 0]
print(even_nums)