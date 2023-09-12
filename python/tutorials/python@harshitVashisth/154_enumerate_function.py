fruits = ["apple", "mango", "banana"]

"""normal code"""
pos = 0
for i in fruits:
    print(f"{pos} => {i}")
    pos += 1
print()

"""enumerate_function"""
for index, fruit in enumerate(fruits):
    print(f"{index} => {fruit}")