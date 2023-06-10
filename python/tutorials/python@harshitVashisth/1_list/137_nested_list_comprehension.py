"""
Task:
    [[123], [123], [123]]
"""
"""example1"""
nested = []
for i in range(1,4):
    nested.append([1, 2, 3])
print(nested)
print()


"""example2"""
nested = [[i for i in range(1,4)] for j in range(3)]
print(nested)