import re

##method-1
#mob = 'My mobile number is: +919006008083'
#mobNo = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
#mo = mobNo.search(mob)
#print('Mobile No.', mo.group())


##method-2
#mob = 'My mobile number is: +919006008083 and office: +919934215315'
#mobNo = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
#mo = mobNo.findall(mob)
#print('Mobile No.', mo)


##method-3
mob = 'My mobile number is: +919006008083 and office: +919934215315'
mobNo = re.compile(r'\+\d\d\d\d\d\d\d\d\d\d\d\d')
mo = mobNo.findall(mob)

for m in mo:
  print('Mobile No.', m)