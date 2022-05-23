#f = open('Files/file.txt', mode='r')
#data = f.readline()
#data2 = f.readline()
#print(data)
#print(data2)
#f.close()

#f = open('Files/file.txt', mode='r')
#data = f.readlines()
#print(data)
#f.close()

#f = open('Files/file.txt', mode='r')
#data = f.readlines()
#for file in data:
#	print(file)
#f.close()

f = open('Files/file.txt', mode='r')
data = f.readlines()
for file in data:
	print(file, end='')
f.close()