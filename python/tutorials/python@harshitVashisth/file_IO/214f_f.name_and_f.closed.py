"""
f.name #check file name with path
f.closed #to check if file is closed or not (in boolean value)
"""
path = "files/file.txt"
f = open(path)

print(f"The file name is:>> {f.name}'") #check file name with path
print(f"The file is closed? {f.closed}") #to check if file is closed or not (in boolean value)
print()

for line in f.readlines():
    print(line, end="")
f.close()
print()

print(f"The file is closed? {f.closed}")