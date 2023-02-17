"""
We can check whether a key is already exists in the dictionary or not, for this purpose we use membership operator.
"""

st = {101:'Rahul',102:'Raj',103:"Sonam"}
print(st)
print()

print(101 in st) #This is return True
print(100 in st) #This is return False
print()

if 101 in st:
    print('101 is exists')