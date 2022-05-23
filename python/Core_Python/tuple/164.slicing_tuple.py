# # Slicing on  tuple can be used to retrieve a piece of the tuple that contains a group of elements. Slicing is useful to retrieve a range of elements.

x = (101,102,103,104,105,106,107)
print(f"Original Tuple: {x}")
print()

a = x[0:]
print(f"From 0th position to last position: {a}")
print()

b = x[1:5]
print(f"From 1st position to 4th position: {b}")
print()


c = x[:5]
print(f"From 0th position to 4th position: {c}")
print()

d = x[-4:]
print(f"Last 4 elements: {d}")
print()

e = x[0:7:2]
print(f"From 0th position to 6th position stride 2: {e}")
print()

f = x[-5:-3]
print(f"Last 5 elements with [-5-(-3)]= 2 elements towards right: {f}")