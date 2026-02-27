import re

"""method-1"""
s = "My mobile number is +919006008083 and my office's number is +919934237649"
num = re.compile(r"\+\d\d\d\d\d\d\d\d\d\d\d\d")

"""single search"""
# mob = num.search(s)
# found = mob.group()
# print(f"Mobile No.:  {found}")

"""multiple search"""
mobs = num.findall(s) #it returns a list
for mob in mobs:
  print(f"Mobile number: {mob}")


##method-3
# mob = 'My mobile number is: +919006008083 and office: +919934215315'
# mobNo = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
# mo = mobNo.findall(mob)

# for m in mo:
#   print('Mobile No.', m)