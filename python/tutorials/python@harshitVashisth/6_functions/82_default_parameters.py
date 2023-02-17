# def user_info(name="unknown", age=None, mob=9006228083):
#     print(f"\tName: {name}")
#     print(f"\tAge: {age}")
#     print(f"\tMobile No.: {mob}")

# user_info()

# user_info("Abdul Zoha")

# user_info("Aftab Alam", 28)

# user_info("Rehan Khan", 30, 9934255334)




"""the default parameters always should be at last"""
def user_info(age, name="unknown", mob=9006228083):
    print(f"\tName: {name}")
    print(f"\tAge: {age}")
    print(f"\tMobile No.: {mob}")

user_info(23)