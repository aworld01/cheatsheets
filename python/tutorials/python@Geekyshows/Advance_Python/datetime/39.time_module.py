'''
Following modules are used to work with date, time, and duration.
1.time
2.datetime

Epoch: The epoch is the point where the time starts, and is platform dependent.
This point is taken as the January 1st of the current year, 00:00:00. For Unix, the epoch is January 1st 1970, 00:00:00(UTC)

UTC: This is coordinated Universal Time (formerly known as Greenwich Mean Time, or GMT). The acronym UTC is not a mistake but a compromise between English and French.

DST: This is Daylight Saving Time, an adjustment for the timezone by (usually) one hour during part of the year. DST rules are magic (derermined by local law) and can change from year to year.

time() function: This function returns the time in seconds since the epoch as a floating point number. The specific date of the epoch and the handling of leap seconds is platform dependent.

ctime() function: This function is used to get current date and time. When we pass epoch time in seconds to the function, it returns corresponding date and time is string format.

localtime() function: This function is used to convert seconds into date and time. It returns an object struct_time which can be used to access the attributes either using an index or using a name.
'''

from time import time, ctime, localtime

# epoch = time() #to print seconds
# print(epoch)

# et = ctime(epoch) #to print date and time
# print(et)



# tim = ctime() #to print current time
# print(tim)



# stobj = localtime() #this will return struct_time object
# print(stobj)
# print(stobj.tm_year) #to print year.

# print('Year:', stobj.tm_year)
# print('Month:', stobj.tm_mon)
# print('Date:', stobj.tm_mday)
# print('Hour:', stobj.tm_hour)
# print('Minute:', stobj.tm_min)
# print('Second:', stobj.tm_sec)

t = localtime()
##date
print('Date:', end="")
print(t.tm_mday, end='/')
print(t.tm_mon, end='/')
print(t.tm_year)
##time
print('Time:', end="")
print(t.tm_hour, end=':')
print(t.tm_min, end=':')
print(t.tm_sec)