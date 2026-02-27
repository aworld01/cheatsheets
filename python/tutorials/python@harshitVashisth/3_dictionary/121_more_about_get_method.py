# usr = {"name": "Abdul Zoha", "age":29}

# name = usr.get("name")
# print(name)

"""to overwrite None"""
# name = usr.get("names", "not found")
# print(name)



"""dictionary automaticaly overwrites the duplicate values"""
usr = {"name": "Abdul Zoha", "age": 29, "name": "Harshit Vashisth"}
print(usr)