'''
datetime: It handles date and time. It has year, month, day, hour, minute, second, microscond and tzinfo attributes.

date: It handles date of gregorian calendar, without taking time zone into  consideration. It has year, month and day attributes.

time: It handles time assuming that every day has exactly 24 x 60 X 60 seconds. It has hour, minute, second, microsecond and tzinfo attributes.

timedelta: It handles durations. The duration may be the difference between two date, time or datetime instances.

datetime object: A datetime object is a single object containing all the information from a date object and a time object.



CREATING OBJECT OF DATETIME CLASS
object_name = datetime(year, month, day, hour=0, minute=0, microsecond=0, tzinfo=None, *, fold=0),

The year, month and day arguments are required. tzinfo may be None, or an instance of a tzinfo subclass. The remaining arguments may be integers, in the following ranges:
MINYEAR <= year <=  MAXYEAR,
1 <= month <= 12,
1 <= day <= number of days in the given month and year,
0 <= hour < 24,
0 <= minute < 60,
0 <= second < 60,
0 <= microsecond < 1000000,
fold in [0, 1].

The fold parameter specifies whether there was any fold in time. A fold in time means a reverse back of the clock time. In conuntries following Daylight Saving time during the end of summer clocks are reversed back by 1 hour. This reverse back is a fold in time.

* means a splat operator. Using a splat operator a tuple can be unpacked and a time object can be constructed out of the values from the tuple.
'''
# from datetime import datetime

# dt1 = datetime(year=2021, month=4, day=11)
# print(dt1)

# dt2 = datetime(year=2021, month=4, day=11, hour=14, minute=23)
# print(dt2)

# dt3 = datetime(2021, 4, 28) #have to follow the order
# print(dt3)

# dt4 = datetime(2021, 4, 11, 15, 30) #have to follow the order
# print(dt4)

# print(dt1.year)



'''
DATETIME CLASS'S METHODS
today(): This method is used to get the current date and time. It returns the date and time information.
Ex:
datetime.today()

now(): This method is used to get the current date and time. We can provide timezone information to this method. If the timezone is not provided, then it takes the local time zone. It returns an object that contains date and time information in any time zone. We can use day, month, year, hour, minute and second.
Ex:
datetime.now()
'''
from datetime import datetime

# ct = datetime.now()
# print(ct)
# print(ct.day)
# print(ct.month)
# print(ct.year)

td = datetime.today()
print(td)
print(td.minute)