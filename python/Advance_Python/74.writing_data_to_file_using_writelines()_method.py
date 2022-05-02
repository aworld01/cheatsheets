'''
writelines(): This method is used to store/write group of string (list, tuple, set) into the file represented by the file object.
'''
f = open("Files/file.txt", mode="w")
s = ["Raju","Sumit","Rohan","Raj"]
f.writelines(s)
f.close()