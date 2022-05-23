def validate(name):
    if len(name) < 8:
        raise ValueError("Name is too short")

usr_name = input("Enter your name: ")
validate(usr_name)
print(f"Hello {usr_name}")