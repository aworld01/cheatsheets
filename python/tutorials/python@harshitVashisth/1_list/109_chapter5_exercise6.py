l =[1,2,3,[3,4],[6,7,7]]
print(l)

def list_count(l):
	count=0
	for i in l:
		if type(i) == list:
			count+=1
	return count
print(list_count(l))