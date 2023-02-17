from numpy import *

# # Without index
# stu_roll = array([101, 102, 103, 104, 105])
# for element in stu_roll:
#     print(element)

# # With index
# stu_roll = array([101, 102, 103, 104, 105])
# n = len(stu_roll)
# for i in range(n):
#     print(stu_roll[i])

stu_roll = array([101, 102, 103, 104, 105])
n = len(stu_roll)
for i in range(n):
    print(f'Index: {i} = {stu_roll[i]}')