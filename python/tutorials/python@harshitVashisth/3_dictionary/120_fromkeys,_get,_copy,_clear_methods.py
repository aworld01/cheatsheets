"""
.fromkeys() method
output = {"name": "unknown","age": "unknown", "height": "unknown"}
"""
"""example-1"""
# d = dict.fromkeys(
#     ["name", "age", "height"], "unknown"
# )
# print(d)

"""example-2"""
# d = dict.fromkeys(
#     ("name", "age", "height"), "unknown"
# )
# print(d)

"""example-3"""
# d = dict.fromkeys(
#     "abc", "unknown"
# )
# print(d)

"""example-4"""
# d = dict.fromkeys(
#     range(1,11), "unknown"
# )
# print(d)




"""
.get() method
None = False
"""
# usr_info = {
#     "name": "Abdul Zoha",
#     "age": 29
# }
## print(usr_info["names"]) #this will throw error

# print(usr_info.get("namew")) #this will return none

# if usr_info.get("namew"):
#     print("Present")
# else:
#     print("Not present")




""".clear() method"""
# usr_info = {
#     "name": "Abdul Zoha",
#     "age": 29
# }

# print(usr_info)
# print()
# usr_info.clear() #to clear the dictionary
# print(usr_info)




""".copy() method"""
usr_info = {
    "name": "Abdul Zoha",
    "age": 29
}

"""example-1"""
# duplicate = usr_info.copy() #to copy the dictionary
# shadow = usr_info
# print(usr_info, id(usr_info))
# print(duplicate, id(duplicate))
# print(shadow, id(shadow))


"""example-2"""
# duplicate = usr_info.copy() #to copy the dictionary
# shadow = usr_info
# print(usr_info, id(usr_info))
# print(duplicate, id(duplicate))
# print(shadow, id(shadow))
# print()
# usr_info.pop("name")
# print(usr_info, id(usr_info))
# print(duplicate, id(duplicate))
# print(shadow, id(shadow))

"""example-3"""
duplicate = usr_info.copy() #to copy the dictionary
shadow = usr_info
print(usr_info is duplicate) #these are not same
print(usr_info is shadow) #these are the same