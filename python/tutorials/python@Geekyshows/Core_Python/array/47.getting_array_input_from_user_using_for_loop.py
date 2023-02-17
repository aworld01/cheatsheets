from array import *

stu_roll = array('i',[])
n = int(input('How many elements? '))
for i in range(n):
    stu_roll.append(int(input('Enter the element: ')))
print(stu_roll)


# stu_roll = array('i',[])
# n = int(input('How many elements? '))
# for i in range(n):
#     stu_roll.append(int(input('Enter the element: ')))
# for i in range(len(stu_roll)):
#     print(stu_roll[i])