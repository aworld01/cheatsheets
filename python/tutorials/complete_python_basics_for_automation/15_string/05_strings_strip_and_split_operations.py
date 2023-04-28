string1 = " python "
string2 = "***python***"
string3 = "Hello world, how are you?"
string4 = "python is very popular lnaguage. It is very easy"

""".strip method (it removes occurrences from sides)"""
# newString1 = string1.strip() #to remove both side of same occurrence (dafult is " ")
# newString2 = string2.strip("*") #to remove stars from both sides of same occurrence
# newString3 = string2.lstrip("*") #to remove stars from left side of same occurrence
# newString4 = string2.rstrip("*") #to remove stars from right side of same occurrence
# """printing results"""
# print(string1)
# print(string2)
# print(newString1)
# print(newString2)
# print(newString3)
# print(newString4)

""".split method"""
newString1 = string3.split() #to split into list (dafult is " ")
newString2 = string3.split(",") #to split from ","
newString3 = string4.split("is") #to split from "is"
"""printing results"""
print(newString1)
print(newString2)
print(newString3)