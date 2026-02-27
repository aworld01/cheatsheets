path = "files/file.txt"

f = open(path)
# print(f.readlines()) #read all the lines of document and returns a list

"""f.readlines() with for loop"""
# for line in f.readlines():
#     print(line)

"exmple-2"
for line in f.readlines():
    print(line, end="") #end="" (to remove extra line between)
f.close()