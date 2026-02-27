"""
update() method overwrites duplicate entries.
update() method never delete existing data.
"""
usr_info = {
    "name": "Harshit Vashisth",
    "age": 30,
}
more_info = {
    "state": "Bihar",
    "name": "Abdul Zoha",
    "hobies":["Coding", "Reading"]
}

# print(usr_info)

usr_info.update(more_info) #to update
print(usr_info)