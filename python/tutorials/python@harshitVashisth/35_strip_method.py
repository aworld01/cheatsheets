name="    Abdul Zoha    "
dots="........"

# left=dots+name
# right=name+dots
# print(left)
# print(right)

# ls=name.lstrip() #to strip left
# rs=name.rstrip() #to strip right
# lplus=dots+ls
# rplus=rs+dots

# print(lplus)
# print(rplus)

# st=name.strip() #to strip left and right
# s=dots+st+dots
# print(s)



# plus=dots+name+dots
# print(plus)

# rep=plus.replace(".","#")
# print(rep)

# rep=plus.replace(" ","") #to replace all the spaces from the string
# print(rep)





name, char=input("Enter name and character separared by comma: ").split(",")
name=name.lower().strip()
char=char.lower().strip()
lenght=len(name)
count=name.count(char)
print(f"Length of your name is: {lenght}")
print(f"Character count: {count}")