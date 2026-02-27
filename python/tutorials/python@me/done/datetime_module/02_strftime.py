from datetime import datetime

today = datetime(2012,6,5,14,43,53) #year,month,day,hour,minute,second
print(today)
print()


"""examples"""
print(today.strftime("%a")) #Mon
print(today.strftime("%A")) #Monday
print()

print(today.strftime("%b")) #Sep
print(today.strftime("%B")) #September
print()

print(today.strftime("%C")) #20 (Century)
print()

print(today.strftime("%d")) #04 (Day)
print(today.strftime("%e")) #4 (Day)
print()

print(today.strftime("%g")) #12 (Year)
print(today.strftime("%G")) #2012 (Year)
print()

print(today.strftime("%h")) #Sep (Month)
print()

print(today.strftime("%H")) #00 (00-23) Hour
print()

print(today.strftime("%j")) #157 (001-366) Day of the year
print()

print(today.strftime("%m")) #06 (01-12) Month
print()

print(today.strftime("%M")) #43 (00-59) Minute
print()

print(today.strftime("%p")) #AM/PM
print()

print(today.strftime("%R")) #14:43 (Hour:Minute)
print()

print(today.strftime("%S")) #53 (00:59) Seconds
print()

print(today.strftime("%T")) #14:43:53 (Time)
print()

print(today.strftime("%r")) #02:43:53 PM (Time)
print()

print(today.strftime("%x")) #06/05/12 (date)
print()

print(today.strftime("%D")) #06/05/12 (date)
print()

print(today.strftime("%u")) #2 (1-7) Weekend
print()

print(today.strftime("%U")) #23 (01-53) Week of the year
print()

print(today.strftime("%V")) #23 (01-53) Week of the year
print()

print(today.strftime("%W")) #23 (01-53) Week of the year
print()

print(today.strftime("%w")) #1 (1-7) Week
print()

print(today.strftime("%y")) #12 (00-99) Year
print()

print(today.strftime("%Y")) #2012 (Year)
print()

print(today.strftime("aha %n ahak")) #Newline charector
print()

print(today.strftime("%t abc")) #Tab charector
print()





"""exercise"""
# date = today.strftime("%d/%m/%y")
# time = today.strftime("%H:%M:%S")
# dt = today.strftime("%r")
# day = today.strftime("%A")

# print(date)
# print(time)
# print(dt)
# print(day)