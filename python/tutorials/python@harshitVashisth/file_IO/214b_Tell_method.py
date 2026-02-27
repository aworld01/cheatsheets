path = "files/file.txt"

f = open(path)
print(f"\tCursor position: {f.tell()}") #to check cursor position
data = f.read()
print(data)
print(f"\tCursor position: {f.tell()}")
f.close()