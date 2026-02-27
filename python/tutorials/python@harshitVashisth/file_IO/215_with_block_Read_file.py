"""
The with statement can be used while opening a file.
When we open afile using with statement, there is no need to close the file explicity.

with open(path, mode="r") as rf: #default mode="r" (read mode)
with open(path) as rf: #default mode="r" (read mode)
"""

path = "files/file.txt"
with open(path) as rf: #default mode="r" (read mode)
    print(rf.read())

    print(f"The file is closed? {rf.closed}") #to check if file is closed or not (in boolean value)
print(f"The file is closed? {rf.closed}")