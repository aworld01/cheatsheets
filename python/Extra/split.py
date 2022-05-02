import os
l = os.listdir()

#print(p)

#for e in l:
#	print(e)
	
#for e in l:
#	s = e.split('.') #for split file by '.'
#	print(e)

#for e in l:
#	s = e.split(".")[-1]
#	print(f"File name is {e} and the extension is: {s}")

for e in l:
	s = os.path.splitext(e)
	print(s)