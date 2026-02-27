import os

#c = os.path.isfile("file.txt")
#print(c)

if os.path.isfile("file.txt"):
	f = open("file.txt")
	print("File opened")
	f.close()
else:
	print("File not found")