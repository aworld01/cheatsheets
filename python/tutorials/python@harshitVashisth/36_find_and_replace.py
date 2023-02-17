'''
replace()
'''
# string="She is beautiful and she is a good dancer"
# print(string)
# print()

# string1=string.replace(" ","_") #to replace all spaces into underscore
# print(string1)
# print()

# string2=string.replace("is","was") #to replace all is into was
# print(string2)
# print()

# string3=string.replace("is","was", 1) #to replace one is into was
# print(string3)


'''
find() #to find position of index
'''
# string="She is beautiful and she is a good dancer"
# print(string)

# pos=string.find("is") #"is" is at 4th position
# print(pos)

# pos1=string.find("is", 5) #to find after 4th position
# print(pos1)


string="She is beautiful and she is a good dancer"
is_pos=string.find("is")
print(is_pos)
  
is_pos2=string.find("is", is_pos+1)
print(is_pos2)