##first read then write. It will append existing data
#f = open('Files/file.txt', mode='r+')
#data = f.read()
#f.write('Hello Artificialworld')
#print(data)


##first write then read. It will overwrite existing data
#f = open('Files/file.txt', mode='w+')
#f.write('Hello Artificialworld01')
#f.seek(0) #to move cursor at 0 position.
#data = f.read()
#print(data)


##first append then read. It won't' overwrite existing data
f = open('Files/file.txt', mode='a+')
f.write(', how are you?')
f.seek(0) #to move cursor at 0 position.
data = f.read()
print(data)