"""
r = read mode(default)
w = write mode
a = append mode
"""
f = open("Files/file.txt", mode="r", encoding="utf-8")
#check = f.name #to check file name
#print(check)

#check = f.mode #to check file mode
#print(check)

#check = f.readable() #to check file is readable or not
#print(check)

#check = f.writable() #to check file is writable or not
#print(check)

#check = f.closed #to check file is closed or not
#print(check)
#f.close() #to close the file
#check = f.closed
#print(check)