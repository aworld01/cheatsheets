import re

##method-1
#mob = 'My mobile number is: +919006008083'
#mobNo = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
#mo = mobNo.search(mob)
#print('Mobile No.', mo.group())


##method-2
#mob = 'My mobile number is: +919006008083'
#mobNo = re.compile(r'(\+\d\d)(\d\d\d\d\d\d\d\d\d\d)')
#mo = mobNo.search(mob)
#print('Mobile No.', mo.groups())
#print('Country Code:', mo.group(1))
#print('Mobile No.', mo.group(2))


##method-3
#mob = 'My mobile number is: +919006008083'
#mo = re.search(r'(\+\d\d)(\d\d\d\d\d\d\d\d\d\d)', mob)
#print('Mobile No.', mo.groups())
#print('Country Code:', mo.group(1))
#print('Mobile No.', mo.group(2))


##method-3
def getMob(s):
  mobNo = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
  mo = mobNo.findall(s)
  if mo:
    return mo
  else:
    return None
    
s='Hello world +919006228083 I am fine'
print(getMob(s))