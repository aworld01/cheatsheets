# == : value equality (Two objects have the same value)
# is : reference equality(Two references refer to the same object)

a = [6,4,"34"]
b = [6,4,"34"]
c = a
print(b == a)
print(b is a)
print(c is a)