"""
dictionary is a data_structure.
Because of limitations of lists, lists are not enough to represent real life data.
dictionary is unordered collections of data in key : value pair.

we can store any datatype in dictionary.
example: numbers, strings, list, dictionary.
"""

"""how to create dictionaries"""
# user = {"name":"Abdul Zoha", "age":28} # key : value
# print(user, type(user))

"""create dictionary using dic() method"""
# user = dict(name = "Harshit Vashisth", age = 29)
# print(user, type(user))



"""
access data from dictionary
NOTE: There is no indexing because of unordered collections of data.
"""
# user = dict(name = "Harshit Vashisth", age = 29)
# name = user["name"] #to access name
# print(name)


"""clean syntax"""
# user = {
#     "name":"Abdul Zoha",
#     "age":28,
#     "vill":"Chandpali"
#     }
# print(user)



"""we can store any datatype in dictionary."""
# user_info = {
#     "name":"Abdul Zoha",
#     "age":28,
#     "vill":"Chandpali",
#     "fav_movies":["coco", "kimi no na wa"],
#     "fav_tunes":["awakening", "fairy tale"]
#     }
# print(user_info)

# fav_tunes = user_info["fav_tunes"]
# print(fav_tunes)



"""add data in dictionary"""
user_info = {} #to assign an empty dictionary
print(user_info)

user_info["name"] = "Abdul Zoha" #to add data
user_info["age"] = 29
print(user_info)