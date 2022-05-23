'''
date object: A date object is an object containing information of year, month and day.

CREATING OBJECT OF DATE CLASS
object_name = date(year, month, day)

All arguments are required. Arguments may be integers, in following range:-

MINYEAR >= year <= MAXYEAR
1 >= month <= 12
1 >= day <= number of days in the given month and year
Ex:
	d = date(year=2021, month=6, day=30)
	
today() method: This method is used to get the current date. It returns only date.
Ex:
	date.today()
'''

from datetime import date

#d1 = date(year=2021, month=4, day=13)
#print(d1)

#d2 = date(2021, 4, 30) #you have to follow the order
#print(d2)
#print(d2.year)

cdate = date.today()
print(cdate)
print(cdate.year)