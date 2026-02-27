"""with the help of list comprehension we can create of list in one line"""

"""example-1"""
"""create a list of squares from 1 to 10"""
# squares = []
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

"""list comprehension"""
# square2 = [i**2 for i in range(1, 11)]
# print(square2)



"""example-2"""
"""print negative numbers"""
# negative = []
# for i in range(10, 0, -1):
#     negative.append(i)
# print(negative)

# """list comprehension"""
# new_negative = [i for i in range(10, 0, -1)]
# print(new_negative)



"""example-3"""
names = ["Harshit", "Mohit", "Rohit"]

"""print first charector"""
new = []
for name in names:
    new.append(name[0])
print(new)

"""list comprehension"""
new2 = [name[0] for name in names]
print(new2)