'''
We can compare date class and datetime class objects using ==, <, >.
The comparison will return either True or False.
d1 = date(year=2018, month=7, day=16)
d2 = date(year=2021, month=7, day=16)
d1 == d2
d1 < d2
d1 > d2
d1 != d2
'''

from datetime import date
d1 = date(year=2018, month=7, day=16)
d2 = date(year=2021, month=7, day=16)
print(d1 == d2)
print(d1 < d2)
print(d1 > d2)
print(d1 != d2)