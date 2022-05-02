"""
module: Python file contains useful classes and functions wrote by developer is called module.

According to wikipedia, Debugging is the process of finding and resolving defects or problems within a computer program that prevent correct operation of computer software or a system.

WHY DEBUGGING?
1. Our program is not running and causing unexpected errors.
2. Our program is working fine but not working the same way we want.

STEPS FOR DEBUGGING
1. set trace
2. execute code line by line

pdb.set_trace() #to trace errors
l #to know line number
n #to goto next line
name #to check variable exists or not
c #to continue your code
"""

import pdb #to import Python debugger

pdb.set_trace() #to trace errors
name=input("Please enter your name: ")
age=input("Please enter your age: ")
print(f"Hello {name} your age is {age}")
age2=int(age)+5
print(f"{name} you will be {age2} in next five years")