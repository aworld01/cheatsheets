"""
print(f.readline()) #to read a singleline
print(f.readline(), end="") #end="" (to remove extra line between)
"""
path = "files/file.txt"

f = open(path)

"""example-1"""
# print(f.readline()) #to read a singleline
# print(f.readline())

"""example-2"""
print(f.readline(), end="") #end="" (to remove extra line between)
print(f.readline(), end="")

f.close()