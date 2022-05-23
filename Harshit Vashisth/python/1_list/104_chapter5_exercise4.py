"""Example-1"""
# numbers=list(range(1,8))
# print(numbers)

# def filter(num):
#     even=[]
#     odd=[]
#     for i in num:
#         if i%2: #to get odd number
#             odd.append(i)
#         else:
#             even.append(i)
#     odd_even=[odd, even]
#     return odd_even
# print(filter(numbers))



"""Example-2"""
numbers=list(range(1,8))
print(numbers)

def filter(num):
    even=[]
    odd=[]
    for i in num:
        if i%2 == 0: #to get even number
            even.append(i)
        else:
            odd.append(i)
    odd_even=[odd, even]
    return odd_even
print(filter(numbers))