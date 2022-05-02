#a = [10,20,30,[40,50,60]]
#n = len(a)
#i = 0
#while i < n:
#  ##checking a[i] is a list type or not
#  if type(a[i]) is list:
#    if len(a[i]) > 1:
#      j = 0
#      m = len(a[i])
#      while j < m:
#        print(i, j, a[i][j])
#        j += 1
#      i += 1
#  else:
#    print(i, a[i])
#    i += 1

 
a = [[10,20,30],[40,50,60]]
n = len(a)
i = 0
while i < n:
  j = 0
  while j < len(a[i]):
    print(i, j, a[i][j])
    j += 1
  i += 1