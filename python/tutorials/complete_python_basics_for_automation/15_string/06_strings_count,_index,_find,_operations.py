string = "Hello world"

""".count() method (returns 0 if not found)"""
# newString = string.count("i") #to count "o"
# """printing results"""
# print(string)
# print(newString)




""".index() method (returns index of first occurrence. returns error if notFound returns error if outOfRange.)"""
# newString1 = string.index("o") #to find first occurrence (returns result in integer)
# newString2 = string.index("o",5) #to find next occurrence
# """printing results"""
# print(newString1)
# print(newString2)

"""dynamic way"""
# newString1 = string.index("o") #to find first occurrence (returns result in integer)
# newString2 = string.index("o", newString1+1) #to find next occurrence
# """printing results"""
# print(newString1)
# print(newString2)




""".find() method (returns index of first occurrence. returns -1 if notFound. returns -1 if outOfRange.)"""
# newString1 = string.find("o") #to find first occurrence (returns result in integer)
# newString2 = string.find("o",175) #to find next occurrence
# """printing results"""
# print(newString1)
# print(newString2)

"""dynamic way"""
newString1 = string.find("o") #to find first occurrence (returns result in integer)
newString2 = string.find("o", newString1+1) #to find next occurrence
"""printing results"""
print(newString1)
print(newString2)