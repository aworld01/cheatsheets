usr_info = {
    "name": "Abdul Zoha",
    "age": 29,
    "vill": "Chandpali",
    "fav_movies": ["Coco", "Kimi no na wa"],
    "fav_tunes": ["Awakening", "Fairy tale"]
}
print(usr_info)

# print()
# """how to add data"""
# usr_info["fav_songs"] = ["Song1", "Song2"] #to add data
# print(usr_info)

# usr_info["dist"] = "Siwan" #to add data
# print(usr_info)




# print()
# """.pop() method"""
# popped_item = usr_info.pop("vill") #to pop item
# print(usr_info)
# print(f"popped item is: {popped_item}")
# print(type(popped_item))




print()
""".popitem() method"""
popped_item = usr_info.popitem() #to pop any random key:value in tuple form
print(usr_info)
print(f"popped item is: {popped_item}")
print(type(popped_item))