'''
timedelta object: A timedelta object represents a duration, the defference between two dates or times.
It's possible to know the future dates or previous dates using timedelta.

CREATING OBJECT OF TIMEDELTA CLASS
object_name = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minuts=0, hours=0, weeks=0)

All arguments are optional and default to 0. Arguments may be integers or floats, and may be positive or negative.

Only days, seconds and microseconds are stored internally. Arguments are converted to those units.
A millisecond is converted to 1000 microseconds.
A minute is converted to 60 seconds.
An hour is converted to 3600 seconds.
A week is converted to 7 days.
Ex:
td = timedelta(days=10)
'''

from datetime import timedelta, date

# td1 = timedelta()
# print(td1)

# td2 = timedelta(days=10)
# print(td2)

## to get future date
td = timedelta(days=20)
d = date.today()
result = d+td
print(result)

## to get past date
result2 = d-td
print(result2)