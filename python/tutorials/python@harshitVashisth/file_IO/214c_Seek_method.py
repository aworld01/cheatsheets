path = "files/file.txt"

f = open(path)
print(f"\tCursor position: {f.tell()}")
data = f.read()
print(data)
print(f"\tCursor position: {f.tell()}")

f.seek(50) #to move cursor at 50th charecter

print("After Seek")
print(f"\tCursor position: {f.tell()}")
data2 = f.read()
print(data2)
print(f"\tCursor position: {f.tell()}")

f.close()