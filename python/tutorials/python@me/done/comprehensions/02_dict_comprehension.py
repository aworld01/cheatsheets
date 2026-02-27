fruits = ["apple", "mango", "banana", "orange", "banana", "apple", "mango", "apple"]

"""simple code"""
# count_occur = {}
# for i in fruits:
#     count_occur.update({i:fruits.count(i)})
# print(count_occur)

"""comprehension"""
# count_occur2 = {i:fruits.count(i) for i in fruits}
# print(count_occur2)



"""comprehension with if-else"""
odd_even = {}
for i in range(1,11):
    if i%2==0:
        odd_even.update({i:"even"})
    else:
        odd_even.update({i:"odd"})
print(odd_even)

"""comprehension"""
odd_even2 = {i:"even" if i%2==0 else "odd" for i in range(1,11)}
print(odd_even2)