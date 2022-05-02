"""
write(): This method is used to store/write charecter or string into the file represented by the file object. It retuens the number of charecter written.
"""
#f = open("Files/file.txt", mode="w")
#f.write("hello world")
#f.close()

#f = open("Files/file.txt", mode="w")
#f.write("Hello")
#f.write("world")
#f.write("how are you?")
#f.close()

f = open("Files/file.txt", mode="w")
f.write("Hello\n")
f.write("world\n")
f.write("how are you?")
f.close()

