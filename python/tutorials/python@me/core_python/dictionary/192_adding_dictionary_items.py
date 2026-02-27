"""
We can add an item to dictionary just by mentioning a new key-value pair into an existing dictionary.
If we mention a key which is already exists in the dictionary then the value gets updated/modified rather then adding a new item.
The new item may be added at any place in the dictionary as dictionary is an unordered collection.
"""
st = {101:'Rahul',102:'Raj',103:'Sonam'}

print(f"\tBefore modification")
print(f"ID: {id(st)}") #to print memory address
print(st)
print()

st[104] = 'Abdul Zoha' #adding an item.

print(f"\tAfter modification:")
print(f"ID: {id(st)}") #to print memory address
print(st)