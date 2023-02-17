#f = open('Files/file.txt', mode='r')
#data = f.read()
#print(data)
#f.close()

f = open('Files/file.txt', mode='r')
data = f.read(2) #to read only two charecters
print(data)
data = f.read(2) #read next two charecters.
print(data)
f.close()