from array import *

stu_roll = array('i',[101,102,103,104,105])
print(stu_roll,type(stu_roll))
n = len(stu_roll)
i = 0
while i < n:
    print(f'{i} = {stu_roll[i]}')
    i += 1