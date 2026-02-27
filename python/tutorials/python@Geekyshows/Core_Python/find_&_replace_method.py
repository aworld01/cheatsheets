'''
replace() method
This method is used to replace strings
'''
#string = 'She is beautiful and she is a good dancer'
#print(string)

#string2 = string.replace('is', 'was') #to replace all strings.
#print(string2)

#string3 = string.replace('is', 'was',1) #to replace only 1st string.
#print(string3)

#string4 = string.replace(' ', '_', 3) #to replace only 3 string.
#print(string4)




'''
find() method
This method is used to find the starting position of any data
'''
string = 'She is beautiful and she is a good dancer'
pos = string.find('is') #to find 1st 'is' position.
print(pos)
pos2 = string.find('is', pos+1) #to find next is position.
print(pos2)