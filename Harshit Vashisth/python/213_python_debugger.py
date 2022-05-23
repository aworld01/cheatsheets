import pdb

"""
l: to know the line number
n: to execute the next line
name: to check if name variable exist or not.
c: to continue the code
"""

pdb.set_trace()
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name} your age is {age}")

age2 = age + 5
print(f"{name} you will be {age2} in next five years..")