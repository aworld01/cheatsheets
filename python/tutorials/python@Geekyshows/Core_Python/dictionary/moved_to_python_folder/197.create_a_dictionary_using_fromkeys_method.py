"""
This method is used to create a new dictionary with the specified keys and values.
Syntax: dict.fromkeys(keys,value)
"""

key = (101, 102, 103)
d = dict.fromkeys(key)
print(d)

key = (101, 102, 103)
value = 'ArtificialWorld'
d = dict.fromkeys(key,value)
print(d)

key = (101, 102, 103)
value = ('Facebook','Youtube','Instagram')
d = dict.fromkeys(key,value)
print(d)