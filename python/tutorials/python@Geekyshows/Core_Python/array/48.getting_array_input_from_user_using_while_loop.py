from array import *

stu_roll = array('i', [])
n = int(input("Enter number of elements: "))
i = 0
j = 0
while i<n:
    stu_roll.append(int(input("Enter element: ")))
    i += 1
print(stu_roll)