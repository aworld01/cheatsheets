'''
tell(): This method is used to find current position of file pointer from beginning of the file. Position starts from 0.
'''

##to open file
#f = open('Files/file.txt', mode='r')
##to get pointer position.
#t = f.tell()
#print(t)
##to read file data (10 charecter).
#data = f.read(10)
#print(data)
#t = f.tell()
#print(t)
##to read more 15 charecter
#data = f.read(15)
#print(data)
#t = f.tell()
#print(t)
##to close the file.
#f.close()


'''
seek(position): This method is used to move file pointer from one position to another position from beginning of the file. Position starts from 0 and it must be positive integer.
'''

f = open('Files/file.txt', mode='r')
t = f.tell() #to get pointer position
print(t)
s = f.seek(4) #to change pointer position at 4th charecter
print(s) #to print pointer position
data = f.read() #to read data
print(data)
f.seek(2)
data = f.read()
print(data)