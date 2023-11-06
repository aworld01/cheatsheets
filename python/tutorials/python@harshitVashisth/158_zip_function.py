usr = ("user1", "user2", "user3")
name = ("Harshit", "Mohit", "Rohit")
usr2 = ("user1", "user2")
name2 = ("Harshit", "Mohit")

print(zip(usr, name))
print()

print(tuple(zip(usr, name)))
print()


print(tuple(zip(usr, name2)))
print()

print(tuple(zip(usr2, name)))
print()


t = (("user1", "Harshit"), ("user2", "Rahul"), ("user3", "Rashmi"))
print(t)
print()

print(dict(t))