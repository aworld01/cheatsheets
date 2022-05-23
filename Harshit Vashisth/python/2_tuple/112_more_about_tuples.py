"""
1: looping in tuples
2: tuple with one element
3: tuple without parenthesis
4: tuple unpacking
5: list inside tuple
6: some functions that you can use with tuples.
"""
# mixed = (1,2,3,4.2)
# print(mixed)

"""for loop and tuple"""
# for i in mixed:
#     print(i)
"""NOTE: You can use while loop too"""



"""tuple with one element"""
# num = (1)
# print(num, type(num))
# num = (1,)
# print(num, type(num))

# word = ("Apple")
# print(word, type(word))
# word = ("Apple",)
# print(word, type(word))



"""tuple without parenthesis"""
# guitar = "Yamaha", "Baton rouge", "taylor"
# print(guitar, type(guitar))



"""tuple unpacking"""
# guitarist = ("Maneli Jamal", "Eddie Van Dar Meer", "Andrew Foy")
# # print(guitarist)

# # guitarist1, guitarist2, guitarist3 = (guitarist)

# guitarist1, guitarist2, guitarist3 = guitarist
# print(guitarist1)
# print(guitarist2)
# print(guitarist3)



"""list inside tuple"""
# favorites = ("Southern Magnolia", ["Tokyo Ghout Theme", "Landscope"])
# print(favorites)

"""you can update data inside tuple's list"""
# # favorites[1].pop()
# # print(favorites)

# favorites[1].append("We make it")
# print(favorites)



mixed = (5, 2, 13, 55, 8)
print(mixed)

mx = max(mixed) #to get maximum number
print(mx)

mn = min(mixed) #to get minimum number
print(mn)

sm = sum(mixed) #to sum all the numbers
print(sm)