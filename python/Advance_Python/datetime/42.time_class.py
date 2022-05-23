'''
time object: A time object is an object containing information of local time of day, independent of any particular day, and subject to adjustment via tzinfo object.

CREATING OBJECT OF TIME CLASS
object_name = time(hour=0, minut=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

All arguments are optional. tzinfo may be None, or an instance of tzinfo subclass.The remaining arguments may be integers, in the following ranges:-
0 <= hour < 24,
0 <= minute < 60,
0 <= second < 60,
0 <= microsecond < 1000000,
fold in [0, 1].
All default to 0 except tzinfo, which defaults to None.
Ex:-
t = time(hour=6, minut=24, second=36)
'''

from datetime import time
t1 = time()
print(t1)

t2 = time(hour=5, minute=7, second=57)
print(t2)
print(t2.hour)

t3 = time(5,3,35)
print(t3)
print(t3.minute)