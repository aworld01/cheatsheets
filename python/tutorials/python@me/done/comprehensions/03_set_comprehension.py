names = {"rahul", "raju", "ramesh", "kashif", "ahmed"}

"""simple code"""
f_word = set()
for name in names:
    f_word.add(name[0])
print(f_word)


f_word2 = {name[0] for name in names}
print(f_word2)