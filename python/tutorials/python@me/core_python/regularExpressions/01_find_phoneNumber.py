import re

s = "My mobile number is +919006008083 and my office's number is +919934237649"

# num = re.compile(r"\+\d\d\d\d\d\d\d\d\d\d\d\d")
num = re.compile(r"\+\d{12}")

"""single search"""
# mob = num.search(s)
# found = mob.group()
# print(f"Mobile No.:  {found}")

"""multiple search"""
mobs = num.findall(s) #it returns a list
for mob in mobs:
  print(f"Mobile number: {mob}")
