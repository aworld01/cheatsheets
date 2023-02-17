"""
OPEN FILE
f = open(path, mode="r") #default mode="r" (read mode)
f = open(path)

f.read() #to read file

f.tell() #to check cursor position

f.seek(50) #to move cursor at 50th charecter

f.readline() #to read a singleline

f.readlines() #read all the lines of document and returns a list

f.name #check file name with path

f.closed #to check if file is closed or not (in boolean value)

f.close() #to close file

"""