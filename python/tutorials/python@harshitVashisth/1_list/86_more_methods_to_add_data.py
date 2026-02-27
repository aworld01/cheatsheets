"""to insert data into any index position"""
# fruits=["Apple", "Mango"]
# print(fruits)
# fruits.insert(1, "Grapes")
# print(fruits)

"""if any index position will not available the item will be inserted at last"""
# fruits=["Apple", "Mango"]
# print(fruits)
# fruits.insert(10, "Grapes")
# print(fruits)


"""list concatenation"""
# fruits1=["Apple", "Mango"]
# print(fruits1)
# fruits2=["Grapes", "Orange"]
# fruits=fruits1 + fruits2 #to concatenate (join) to lists.
# print(fruits)


"""to add items using extend() method"""
fruits1=["Apple", "Mango"]
print(fruits1)
fruits2=["Grapes", "Orange"]
fruits1.extend(fruits2) #to add fruits2 into fruits1
print(fruits1)


"""to add list into list"""
fruits1=["Apple", "Mango"]
print(fruits1)
fruits2=["Grapes", "Orange"]
fruits1.append(fruits2) #to add fruits2 into fruits1
print(fruits1)