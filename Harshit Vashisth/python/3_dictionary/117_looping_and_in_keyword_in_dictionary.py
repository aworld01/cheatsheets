user_info = {
    "name":"Abdul Zoha",
    "age":28,
    "vill":"Chandpali",
    "fav_movies":["coco", "kimi no na wa"],
    "fav_tunes":["awakening", "fairy tale"]
    }
# print(user_info)



"""check if key exist in dictionary"""
# if "name" in user_info:
#     print("Present")
# else:
#     print("Not present")



"""check if value exist in dictionary"""
# if "Abdul Zoha" in user_info.values():
#     print("Present")
# else:
#     print("Not present")



"""loops in dictionaries"""
# for i in user_info: #to access all keys
#     print(i)


# for i in user_info.values(): #to access all values
#     print(i)

# print()
# for i in user_info: #to access all values
#     print(user_info[i])



""".values() method"""
# values = user_info.values() #to access all values
# print(values)
# print(type(values))



""".keys() method"""
# keys = user_info.keys() #to access all keys
# print(keys)
# print(type(keys))



""".items() method"""
# items = user_info.items() #to access all items
# print(items)
# print(type(items))



"""for loop in items"""
for key, value in user_info.items():
    print(f"Key is: {key} and value is: {value}")