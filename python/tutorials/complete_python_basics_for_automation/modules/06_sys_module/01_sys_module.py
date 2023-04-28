"""
The sys() module is used to work with python runtime environment.
The sys() module provides functions and variables used to manipulate different parts of the Python runtime environment.
"""

import sys

# print(dir(sys)) #to list functions and variables
# help(sys) #to read documentation

"""examples1"""
# print(sys.platform) #to see installed python bit
# print(sys.version) #to see python version
# print(sys.version) #to see python version

"""example2 (to check where python go and check for it requirments)"""
# n = sys.path
# for index, path in enumerate(n):
#     print(f"{index}: => {path}\n")



"""more other examples"""
sys.exit() #to stop python runtime environment
print("Hello world!!!")