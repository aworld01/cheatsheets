from array import *

# # Without index
# stu_roll = array('i',[101,102,103,104,105])
# print(stu_roll,type(stu_roll))

# stu_roll = array('i',[101,102,103,104,105])
# for i in stu_roll:
#     print(i)


# # With index
# stu_roll = array('i',[101,102,103,104,105])
# n = len(stu_roll)
# for i in range(n):
#     print(stu_roll[i])


stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
for i in range(n):
    print(f'{i} = {stu_roll[i]}')