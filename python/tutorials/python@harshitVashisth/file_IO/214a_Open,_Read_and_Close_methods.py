"""
f = open(path, mode="r") #default mode="r" (read mode)
f = open(path) #default mode="r" (read mode)

data = f.read() #to read file
f.close() #to close file
"""
path = "files/file.txt"

# f = open(path, mode="r") #default mode="r" (read mode)
f = open(path)
data = f.read() #to read file

print(data) #to print data
print(type(data)) #to print datatype

f.close() #to close file