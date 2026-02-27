"""We can modify the existing value of key by assigning a new value."""
fees = {'Rahul':2000,'Raj':3000,'Sonam':8000,'raj':1000}

print(f"\tBefore modification")
print(f"ID: {id(fees)}") #to print memory address
print(fees)
print()

fees["Raj"] = 5000 #modify 3000 into 5000.

print(f"\tAfter modification:")
print(f"ID: {id(fees)}")
print(fees)